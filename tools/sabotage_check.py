#!/usr/bin/env python3
"""sabotage_check.py — runs every sabotage tools/README.md describes, each in a fresh scratch copy of this repository,
and requires the named command to FAIL there. Standard library only; needs no network. Writes tools/SABOTAGE-PROOF.md.

    python3 tools/sabotage_check.py            # exit 1 if any sabotage is NOT caught (a claim without a working command)

A claim whose sabotage the command does not catch is decoration, the same way a checker that never fails is.
"""
import os, re, sys, glob, shutil, subprocess, tempfile, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

def fresh():
    tmp = tempfile.mkdtemp(prefix="nfse-auditor-sabotage-")
    dst = os.path.join(tmp, "repo"); shutil.copytree(ROOT, dst, symlinks=True); return dst

def run(cwd, *args):
    r = subprocess.run([PY, *args], cwd=cwd, capture_output=True, text=True); return r.returncode, r.stdout + r.stderr

def edit(path, fn):
    t = open(path, encoding="utf-8").read(); open(path, "w", encoding="utf-8").write(fn(t))

def sab_c1(d):  # one word changed inside a quoted excerpt of a prediction
    p = os.path.join(d, "expected", "nfse-01.md"); lines = open(p, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines):
        c = l.split("|")
        if l.startswith("|") and "PASSA" in l and len(c) >= 8 and len(c[-2].strip()) > 20:
            q = c[-2]; c[-2] = q.replace("a", "e", 1) if "a" in q else q + " x"; lines[i] = "|".join(c); break
    open(p, "w", encoding="utf-8").write("\n".join(lines))
def sab_c0(d):
    f = sorted(glob.glob(os.path.join(d, "reference", "pt", "excerpts", "*.txt")))[0]; open(f, "a", encoding="utf-8").write("x")
def sab_c3_pass(d): edit(os.path.join(d, "expected", "m2-campo-obrigatorio.md"), lambda t: t.replace("FALHA", "PASSA"))
def sab_c3_missing(d): os.remove(os.path.join(d, "expected", "m1-rephrase-b.md"))
def sab_c5_readme(d): edit(os.path.join(d, "README.md"), lambda t: t.replace("What to load: ", "What to load: fixtures/ · ", 1))
def sab_c5_entry(d): open(os.path.join(d, "CLAUDE.md"), "a", encoding="utf-8").write("\nPASSA\n")
def sab_loader(d): edit(os.path.join(d, "tools", "make_load_folder.py"), lambda t: t.replace('LOAD = ["README.md"', 'LOAD = ["fixtures/clean/nfse-01.xml", "README.md"', 1))
def sab_zip(d): open(os.path.join(d, "identity.md"), "a", encoding="utf-8").write("x")
def sab_c6(d):  # a CNPJ with valid check digits, built here so the literal never sits in this file (C6 would catch it)
    base = "112223330001"
    def dv(nums, w): s = sum(int(n) * k for n, k in zip(nums, w)); r = s % 11; return "0" if r < 2 else str(11 - r)
    w1 = [5,4,3,2,9,8,7,6,5,4,3,2]; d1 = dv(base, w1); d2 = dv(base + d1, [6] + w1)
    open(os.path.join(d, "rules.md"), "a", encoding="utf-8").write(f"\nCNPJ {base[:2]}.{base[2:5]}.{base[5:8]}/{base[8:]}-{d1}{d2}\n")
def sab_selftest(d): shutil.copy(os.path.join(d, "tools", "selftest", "good-report.md"), os.path.join(d, "tools", "selftest", "bad-report.md"))
def sab_order(d):  # a new round whose transcript is committed before its prediction
    r = os.path.join(d, "rounds", "round-9-sabotage"); os.makedirs(r)
    g = lambda *a: subprocess.run(["git", *a], cwd=d, capture_output=True, text=True, env={**os.environ, "GIT_AUTHOR_NAME": "sabotage", "GIT_AUTHOR_EMAIL": "s@x", "GIT_COMMITTER_NAME": "sabotage", "GIT_COMMITTER_EMAIL": "s@x"})
    open(os.path.join(r, "transcript.md"), "w").write("# t\n"); g("add", "-A"); g("commit", "-q", "-m", "transcript first")
    open(os.path.join(r, "expected.md"), "w").write("# e\n"); g("add", "-A"); g("commit", "-q", "-m", "prediction after")

def check_order_fails(d):
    import prove_order
    res = prove_order.check_order(d)
    bad = [l for l, ok in res if not ok]
    return (1 if bad else 0), "\n".join(bad) or "(all order checks passed — sabotage NOT caught)"

CASES = [  # (claim in tools/README.md, sabotage, command run in the copy, what must happen)
    ("quotes verbatim (C1)", sab_c1, lambda d: run(d, "tools/check_audit.py")),
    ("excerpts cut from the full texts (C0)", sab_c0, lambda d: run(d, "tools/check_audit.py")),
    ("a mutation's prediction FAILS on its check (C3)", sab_c3_pass, lambda d: run(d, "tools/check_audit.py")),
    ("one prediction per fixture, rephrase included (C3)", sab_c3_missing, lambda d: run(d, "tools/check_audit.py")),
    ("the README's load list never names the evidence (C5)", sab_c5_readme, lambda d: run(d, "tools/check_audit.py")),
    ("the entry file only routes (C5)", sab_c5_entry, lambda d: run(d, "tools/check_audit.py")),
    ("make_load_folder refuses an evidence path", sab_loader, lambda d: run(d, "tools/make_load_folder.py", os.path.join(d, "out"))),
    ("the committed zip is the current files (--check)", sab_zip, lambda d: run(d, "tools/make_load_folder.py", "--check")),
    ("no real identifier (C6)", sab_c6, lambda d: run(d, "tools/check_audit.py")),
    ("predictions before reports, from git (prove_order)", sab_order, check_order_fails),
    ("the checker is not decoration (--selftest)", sab_selftest, lambda d: run(d, "tools/check_audit.py", "--selftest")),
]

def main():
    stamp = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    lines = [f"# SABOTAGE-PROOF — {stamp} — HEAD {head}", "", "Each line: a claim of `tools/README.md`, its sabotage applied to a fresh scratch copy, and the first line the command printed. CAUGHT = the command failed, as the claim says it must.", ""]
    allok = True
    for claim, sab, cmd in CASES:
        d = fresh()
        try:
            sab(d); code, out = cmd(d)
            first = next((l for l in out.split("\n") if l.startswith("FAIL") or "FAIL" in l), out.strip().split("\n")[-1] if out.strip() else "")
            ok = code != 0; allok &= ok
            first = re.sub(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", "[the planted CNPJ]", first)  # the proof file must not carry it either
            lines.append(f"- {'CAUGHT' if ok else 'NOT CAUGHT'}  {claim} — `{first.strip()[:160]}`")
        finally:
            shutil.rmtree(os.path.dirname(d), ignore_errors=True)
    out = "\n".join(lines) + "\n"; print(out)
    open(os.path.join(ROOT, "tools", "SABOTAGE-PROOF.md"), "w", encoding="utf-8").write(out)
    sys.exit(0 if allok else 1)

if __name__ == "__main__": main()
