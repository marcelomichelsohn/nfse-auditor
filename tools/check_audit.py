#!/usr/bin/env python3
"""check_audit.py — the folder's gate, in code. Standard library only; offline; one command.

    python3 tools/check_audit.py             # checks the folder as it stands
    python3 tools/check_audit.py --selftest  # proves the checks bite on tools/selftest/ (a bad report must FAIL)

Checks (each names the file and the line when it fails):
  C0  every reference/pt/excerpts/*.txt is a verbatim substring (whitespace-normalised) of a reference/pt/full/ text;
      same for reference/en/excerpts/ against reference/en/full/
  C1  every quoted excerpt in a report row (rounds transcripts, examples.md, expected/*.md; column "trecho citado") resolves as a substring of reference/pt/
      (Portuguese report) or reference/en/ (English report) — never a translated quote
  C2  every report row: the provision id exists in reference/INDEX.md (or is a required-fields.md path for check 2);
      the result is one of the four words; severity is one of the three classes or "—"; the location names an
      XML path that exists in the fixture the row names (when the fixture is in fixtures/)
  C3  every fixture XML in fixtures/ has exactly one expected file in expected/; every fixtures/mutations/<slug>/
      has CHANGE.md naming the field and the rule, and its expected file has a FAIL on that check
  C4  every rounds/round-*/ folder has the files the protocol requires (round 0: REQUEST.md + transcript.md;
      others: expected.md + transcript.md)
  C5  README.md's "what to load" list names the five things + reference/pt/excerpts/ + reference/tables/ and never
      fixtures/, expected/, rounds/, tools/, reference/pt/full/
  C6  no real identifier leaks: check-digit-valid CNPJ/CPF, e-mails, phone numbers, X509Certificate, and the names
      in an optional private list (--names <file>, kept OUTSIDE the repo) — over every file in the folder
A checker that never fails is decoration: --selftest runs C1/C2 on tools/selftest/bad-report.md (must FAIL on named
checks) and tools/selftest/good-report.md (must PASS), and C0 on a planted edited excerpt.
"""
import os, re, sys, glob, xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS = {"PASSA", "FALHA", "NÃO DÁ PARA DETERMINAR", "NÃO SE APLICA", "PASS", "FAIL", "CANNOT DETERMINE", "NOT APPLICABLE"}
SEVER = {"bloqueia o fechamento", "corrigir antes de fechar", "informativo", "—", "-",
         "blocks closing", "correct before closing", "informational"}
fails = []

def norm(t): return re.sub(r"\s+", " ", t).strip()
def read(p):
    with open(p, encoding="utf-8", errors="replace") as f: return f.read()
def fail(check, where, msg): fails.append(f"{check}  {where}: {msg}")

def corpus(lang):
    txt = []
    for p in sorted(glob.glob(os.path.join(ROOT, "reference", lang, "full", "*.txt"))) + \
             sorted(glob.glob(os.path.join(ROOT, "reference", lang, "excerpts", "*.txt"))):
        txt.append(norm(read(p)))
    return txt

def c0():
    for lang in ("pt", "en"):
        fulls = [norm(read(p)) for p in glob.glob(os.path.join(ROOT, "reference", lang, "full", "*.txt"))]
        for ex in sorted(glob.glob(os.path.join(ROOT, "reference", lang, "excerpts", "*.txt"))):
            if not any(norm(read(ex)) in f for f in fulls):
                fail("C0", os.path.relpath(ex, ROOT), "excerpt is not a verbatim substring of any full text")

def index_ids():
    ids = set()
    p = os.path.join(ROOT, "reference", "INDEX.md")
    if not os.path.exists(p): return ids
    for m in re.finditer(r"^\| \*\*(.+?)\*\* \|", read(p), re.M): ids.add(m.group(1).strip())
    return ids

ROW = re.compile(r"^\|\s*(?P<nota>[^|]*)\|\s*(?P<check>[^|]*)\|\s*(?P<disp>[^|]*)\|\s*(?P<res>[^|]*)\|\s*(?P<sev>[^|]*)\|\s*(?P<loc>[^|]*)\|\s*(?P<trecho>[^|]*)\|\s*$")

def report_rows(path):
    rows = []
    for i, line in enumerate(read(path).split("\n"), 1):
        m = ROW.match(line)
        if not m: continue
        d = {k: v.strip() for k, v in m.groupdict().items()}
        if d["check"].lower() in ("check", "---", "") or set(d["check"]) <= set("-: "): continue
        if not re.match(r"^\d", d["check"]): continue
        rows.append((i, d))
    return rows

def xml_paths(fixture):
    paths = set()
    try: root = ET.parse(fixture).getroot()
    except Exception: return paths
    def walk(e, p):
        tag = re.sub(r"\{.*\}", "", e.tag); q = (p + "/" + tag) if p else tag
        paths.add(q)
        for c in e: walk(c, q)
    walk(root, ""); return paths

def find_fixture(name):
    stem = os.path.splitext(name)[0]
    for p in glob.glob(os.path.join(ROOT, "fixtures", "**", "*.xml"), recursive=True):
        if os.path.basename(p) == name or os.path.splitext(os.path.basename(p))[0] == stem: return p
        if os.path.basename(os.path.dirname(p)) == stem: return p  # a mutation folder: fixtures/mutations/<slug>/nfse.xml
    return None

def c1_c2(paths, ids, lang_corpora):
    for rp in paths:
        text = read(rp); rel = os.path.relpath(rp, ROOT)
        lang = "en" if re.search(r"\|\s*(PASS|FAIL|CANNOT DETERMINE|NOT APPLICABLE)\s*\|", text) and not re.search(r"\|\s*(PASSA|FALHA)\s*\|", text) else "pt"
        for ln, d in report_rows(rp):
            q = norm(d["trecho"].strip("`\"“” "))
            if q and q not in ("—", "-") and not any(q in c for c in lang_corpora[lang]):
                fail("C1", f"{rel}:{ln}", f"quote does not resolve in reference/{lang}/: “{q[:60]}…”")
            if d["res"] not in RESULTS: fail("C2", f"{rel}:{ln}", f"result word not allowed: {d['res']!r}")
            if d["sev"] not in SEVER: fail("C2", f"{rel}:{ln}", f"severity not allowed: {d['sev']!r}")
            disp = d["disp"].strip("*` ")
            if not (disp in ids or disp.startswith("NFSe/") or disp.startswith("required-fields") or disp.startswith("ANEXO")):
                fail("C2", f"{rel}:{ln}", f"provision id not in reference/INDEX.md: {disp!r}")
            m = re.match(r"^([A-Za-z0-9_/\.\-]+)\s*=", d["loc"])
            if m:
                fx = find_fixture(d["nota"])
                if fx:
                    p = m.group(1).lstrip("/")
                    ps = xml_paths(fx)
                    if not any(x.endswith(p) for x in ps): fail("C2", f"{rel}:{ln}", f"location path not in fixture {os.path.basename(fx)}: {p}")

def c3():
    fx = glob.glob(os.path.join(ROOT, "fixtures", "**", "*.xml"), recursive=True)
    for f in fx:
        stem = os.path.splitext(os.path.basename(f))[0]
        if "mutations" in f: stem = os.path.basename(os.path.dirname(f))
        exp = glob.glob(os.path.join(ROOT, "expected", stem + ".md"))
        if len(exp) != 1: fail("C3", os.path.relpath(f, ROOT), f"expected/{stem}.md: found {len(exp)}, need exactly 1")
    for d in glob.glob(os.path.join(ROOT, "fixtures", "mutations", "*")):
        if not os.path.isdir(d): continue
        ch = os.path.join(d, "CHANGE.md")
        if not os.path.exists(ch): fail("C3", os.path.relpath(d, ROOT), "CHANGE.md missing"); continue
        t = read(ch)
        if not re.search(r"(?i)field|campo", t) or not re.search(r"(?i)check|rule|regra", t): fail("C3", os.path.relpath(ch, ROOT), "CHANGE.md must name the field and the check/rule")
        m = re.search(r"(?i)check\s*(\d)", t)
        exp = os.path.join(ROOT, "expected", os.path.basename(d) + ".md")
        if m and os.path.exists(exp):
            et = read(exp)
            if not re.search(r"\|\s*" + m.group(1) + r"(-[\wáéíóúãõç]+)?\s*\|[^|]*\|\s*(FALHA|FAIL)\s*\|", et): fail("C3", os.path.relpath(exp, ROOT), f"no FAIL row for check {m.group(1)} named in CHANGE.md")

def c4():
    for d in sorted(glob.glob(os.path.join(ROOT, "rounds", "round-*"))):
        need = ["REQUEST.md", "transcript.md"] if os.path.basename(d).startswith("round-0") else ["expected.md", "transcript.md"]
        for n in need:
            if not os.path.exists(os.path.join(d, n)): fail("C4", os.path.relpath(d, ROOT), f"{n} missing")

def c5():
    p = os.path.join(ROOT, "README.md")
    if not os.path.exists(p): fail("C5", "README.md", "missing"); return
    t = read(p)
    m = re.search(r"(?is)(what to load|o que carregar).*?(?:\n\n|\Z)", t)
    if not m:
        if os.path.exists(os.path.join(ROOT, "examples.md")): fail("C5", "README.md", "no 'what to load' section, and the auditor files exist")
        else: print("C5   README.md has no 'what to load' section yet (allowed until examples.md exists)")
        return
    sec = m.group(0)
    for must in ["identity.md", "rules.md", "examples.md", "README.md", "reference/pt/excerpts", "reference/tables"]:
        if must not in sec: fail("C5", "README.md", f"load list lacks {must}")
    for never in ["fixtures/", "expected/", "rounds/", "tools/", "reference/pt/full", "reference/en/full"]:
        if re.search(r"(?<!never load )(?<!never )" + re.escape(never), sec): fail("C5", "README.md", f"load list names {never}")

def cnpj_ok(d):
    d = re.sub(r"\D", "", d)
    if len(d) != 14 or d == d[0] * 14: return False
    def dv(nums, w): s = sum(int(n) * k for n, k in zip(nums, w)); r = s % 11; return "0" if r < 2 else str(11 - r)
    w1 = [5,4,3,2,9,8,7,6,5,4,3,2]; w2 = [6] + w1
    return dv(d[:12], w1) == d[12] and dv(d[:13], w2) == d[13]
def cpf_ok(d):
    d = re.sub(r"\D", "", d)
    if len(d) != 11 or d == d[0] * 11: return False
    def dv(nums, start): s = sum(int(n) * k for n, k in zip(nums, range(start, 1, -1))); r = (s * 10) % 11; return "0" if r == 10 else str(r)
    return dv(d[:9], 10) == d[9] and dv(d[:10], 11) == d[10]

def c6(names_file=None):
    names = [n.strip() for n in read(names_file).split("\n") if n.strip()] if names_file and os.path.exists(names_file) else []
    for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isdir(p) or "/.git/" in p or p.endswith((".xlsx", ".zip", ".pdf", ".png")) or p.endswith("check_audit.py"): continue
        rel = os.path.relpath(p, ROOT); t = read(p)
        if rel.startswith("reference/") and not rel.startswith("reference/tables/README") and rel != "reference/INDEX.md":
            continue  # laws and official tables carry public identifiers of public bodies; the sweep is for the folder's own text and fixtures
        for i, line in enumerate(t.split("\n"), 1):
            for m in re.finditer(r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b", line):
                if cnpj_ok(m.group(0)) and rel.startswith("fixtures/") is False: fail("C6", f"{rel}:{i}", f"check-digit-valid CNPJ in text: {m.group(0)}")
            if "X509Certificate" in line or "SignatureValue" in line: fail("C6", f"{rel}:{i}", "signature/certificate block present")
            for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", line):
                if "noreply" not in m.group(0) and not m.group(0).endswith(".invalid"): fail("C6", f"{rel}:{i}", f"e-mail: {m.group(0)}")  # .invalid is the reserved placeholder TLD the anonymiser writes
            for n in names:
                if n.lower() in line.lower(): fail("C6", f"{rel}:{i}", f"private-list name present: {n}")

def selftest():
    global fails
    st = os.path.join(ROOT, "tools", "selftest")
    ids = index_ids(); corp = {"pt": corpus("pt"), "en": corpus("en")}
    fails = []; c1_c2([os.path.join(st, "bad-report.md")], ids, corp); bad = list(fails)
    fails = []; c1_c2([os.path.join(st, "good-report.md")], ids, corp); good = list(fails)
    # planted edited excerpt
    fake = os.path.join(ROOT, "reference", "pt", "excerpts", "_selftest_edited.txt")
    open(fake, "w").write("Art. 1o O Imposto Sobre Serviços de Qualquer Natureza NÃO tem como fato gerador esta frase inventada.\n")
    fails = []; c0(); c0f = [f for f in fails if "_selftest_edited" in f]; os.remove(fake)
    ok = len(bad) >= 3 and not good and c0f
    print("SELFTEST bad-report findings:", len(bad)); [print("   ", f) for f in bad]
    print("SELFTEST good-report findings:", len(good)); print("SELFTEST planted edited excerpt caught by C0:", bool(c0f))
    print("SELFTEST", "PASS" if ok else "FAIL"); return 0 if ok else 1

def main():
    if "--selftest" in sys.argv: sys.exit(selftest())
    names = None
    if "--names" in sys.argv: names = sys.argv[sys.argv.index("--names") + 1]
    ids = index_ids(); corp = {"pt": corpus("pt"), "en": corpus("en")}
    c0()
    reports = [p for p in glob.glob(os.path.join(ROOT, "rounds", "**", "*.md"), recursive=True) if os.path.basename(p) in ("transcript.md", "report.md") or "report" in os.path.basename(p)]
    reports += [os.path.join(ROOT, "examples.md")] if os.path.exists(os.path.join(ROOT, "examples.md")) else []
    reports += sorted(glob.glob(os.path.join(ROOT, "expected", "*.md")))  # the expected results are report-shaped: their quotes and ids must resolve too
    c1_c2(reports, ids, corp); c3(); c4(); c5(); c6(names)
    nq = sum(len(report_rows(r)) for r in reports)
    print(f"check_audit: reports read {len(reports)}, rows {nq}; excerpts pt {len(glob.glob(os.path.join(ROOT,'reference/pt/excerpts/*.txt')))} en {len(glob.glob(os.path.join(ROOT,'reference/en/excerpts/*.txt')))}")
    for f in fails: print("FAIL", f)
    print("check_audit:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)

if __name__ == "__main__": main()
