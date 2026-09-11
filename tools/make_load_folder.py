#!/usr/bin/env python3
"""make_load_folder.py — builds the operator's folder from this repository. Standard library only.

    python3 tools/make_load_folder.py <out-dir>          # writes <out-dir>/nfse-auditor-carregar/ (flat), .zip beside it, and LEIA-PRIMEIRO.html
    python3 tools/make_load_folder.py --check            # the zip committed in download/ holds exactly the current files, byte for byte (exit 1 if not)

Why it exists: the operator loads the folder into a Claude project, which ignores subfolders and refuses .zip; so the files
that are loaded (the list in README.md § "What to load") are copied flat, with their names checked unique, and zipped for
sending. README.md is also rendered to HTML so it reads on any computer without a markdown viewer. The repository keeps its
structure; this folder is only how it is delivered. Nothing from fixtures/, expected/, rounds/ or tools/ is copied.
"""
import os, re, sys, glob, shutil, html, zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOAD = ["README.md", "CLAUDE.md", "identity.md", "rules.md", "examples.md", "reference/INDEX.md",
        "reference/tables/required-fields.md", "reference/tables/TABLES.md",
        "reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv"]
LOAD += sorted(glob.glob("reference/pt/excerpts/*.txt", root_dir=ROOT)) + sorted(glob.glob("reference/en/excerpts/*.txt", root_dir=ROOT))
LOAD += sorted(glob.glob("reference/tables/working/*.csv", root_dir=ROOT)) + sorted(glob.glob("reference/tables/official/csv/*.csv", root_dir=ROOT))
NEVER = ("fixtures/", "expected/", "rounds/", "tools/", "reference/pt/full/", "reference/en/full/")  # the README's never-load list

def md_to_html(md):
    """A small converter for what README.md uses: #/## headings, paragraphs, numbered lists, **bold**, `code`, links."""
    def inline(t):
        t = html.escape(t, quote=False)
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
        return t
    out, para, inlist = [], [], False
    def flush():
        nonlocal para
        if para: out.append("<p>" + "<br>\n".join(inline(x) for x in para) + "</p>"); para = []
    for line in md.split("\n"):
        if re.match(r"^\d+\. ", line):
            flush()
            if not inlist: out.append(f'<ol start="{int(line.split(".")[0])}">'); inlist = True  # steps 5–7 stay 5–7 in the HTML
            out.append("<li>" + inline(re.sub(r"^\d+\. ", "", line)) + "</li>"); continue
        if inlist and (line.strip() == "" or not re.match(r"^\d+\. ", line)):
            out.append("</ol>"); inlist = False
        if line.startswith("# "): flush(); out.append("<h1>" + inline(line[2:]) + "</h1>")
        elif line.startswith("## "): flush(); out.append("<h2>" + inline(line[3:]) + "</h2>")
        elif line.strip() == "": flush()
        else: para.append(line)
    flush()
    if inlist: out.append("</ol>")
    css = ("body{max-width:860px;margin:32px auto;padding:0 24px;font:16px/1.6 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#1f2328;background:#fff}"
           "h1{font-size:2em;border-bottom:1px solid #d1d9e0;padding-bottom:.3em}h2{font-size:1.5em;border-bottom:1px solid #d1d9e0;padding-bottom:.3em;margin-top:1.5em}"
           "code{background:#f6f8fa;padding:.2em .4em;border-radius:6px;font-size:85%}ol{padding-left:2em}li{margin:.4em 0}")
    return ("<!doctype html><html lang=\"pt-BR\"><head><meta charset=\"utf-8\"><title>nfse-auditor — README</title><style>" + css + "</style></head><body>\n" + "\n".join(out) + "\n</body></html>\n")

def check():
    """The committed download/nfse-auditor-carregar.zip must hold exactly the files LOAD names, with their current bytes."""
    zpath = os.path.join(ROOT, "download", "nfse-auditor-carregar.zip")
    if not os.path.exists(zpath): print("FAIL download/nfse-auditor-carregar.zip missing"); sys.exit(1)
    want = {os.path.basename(p): open(os.path.join(ROOT, p), "rb").read() for p in LOAD}
    with zipfile.ZipFile(zpath) as z:
        have = {os.path.basename(n): z.read(n) for n in z.namelist() if not n.endswith("/")}
    bad = sorted(n for n in want if n not in have or have[n] != want[n]) + sorted(n for n in have if n not in want)
    if bad: print("FAIL the zip in download/ differs from the current files (rebuild: python3 tools/make_load_folder.py download):", bad); sys.exit(1)
    print(f"OK download/nfse-auditor-carregar.zip holds the {len(want)} current files")

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    if sys.argv[1] == "--check": check(); return
    out = os.path.abspath(sys.argv[1]); flat = os.path.join(out, "nfse-auditor-carregar")
    if os.path.exists(flat): shutil.rmtree(flat)
    os.makedirs(flat)
    bad = [p for p in LOAD if p.startswith(NEVER)]
    if bad: print("FAIL these paths are evidence, never loaded (README.md § What to load):", bad); sys.exit(1)
    names = [os.path.basename(p) for p in LOAD]
    dup = sorted({n for n in names if names.count(n) > 1})
    if dup: print("FAIL duplicate file names, a project would merge them:", dup); sys.exit(1)
    for p in LOAD: shutil.copy(os.path.join(ROOT, p), os.path.join(flat, os.path.basename(p)))
    zpath = flat + ".zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for n in sorted(os.listdir(flat)): z.write(os.path.join(flat, n), os.path.join("nfse-auditor-carregar", n))
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f: md = f.read()
    with open(os.path.join(out, "LEIA-PRIMEIRO.html"), "w", encoding="utf-8") as f: f.write(md_to_html(md))
    print(f"{len(LOAD)} files → {flat}\n{zpath}\n{os.path.join(out, 'LEIA-PRIMEIRO.html')}")

if __name__ == "__main__": main()
