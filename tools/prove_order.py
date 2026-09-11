#!/usr/bin/env python3
"""prove_order.py — proves, from git history (never from file times), the order this repository claims. Stdlib only.

    python3 tools/prove_order.py            # runs (i)+(ii)+(iii), writes rounds/ORDER-PROOF.md, exit 1 on any FAIL
    python3 tools/prove_order.py --verify   # read-only: (ii)+(iii) only, nothing written — run after the push

(i)   order:   rounds/round-0-by-hand/REQUEST.md was first committed before any of identity.md, rules.md, examples.md, reference/;
               for every rounds/round-N-*/ (N>=1): expected.md first-committed before transcript.md; round N before round N+1;
               expected/ and fixtures/ first-committed before examples.md; rounds/control-*/, rounds/refusal*/ and rounds/walk-*/: expected before transcript (a walk is a witness from outside the office; it is checked like a control, not as a numbered round)
(ii)  remote:  after `git fetch`, HEAD == origin/main and the working tree is clean (nothing pending, nothing unpushed)
(iii) clone:   a fresh `git clone` of the remote into a new temporary folder reproduces the same first-commit order (i) and
               tools/check_audit.py passes there
Sequence at a close: prove_order.py -> commit rounds/ORDER-PROOF.md -> push -> prove_order.py --verify
"""
import os, re, sys, glob, subprocess, tempfile, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def git(*a, cwd=ROOT):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True).stdout.strip()
def first_commit_time(path, cwd=ROOT):
    out = git("log", "--diff-filter=A", "--follow", "--format=%ct %h", "--", path, cwd=cwd).split("\n")
    out = [o for o in out if o.strip()]
    if not out: return None, None
    t, h = out[-1].split(); return int(t), h

def check_order(cwd):
    res = []
    req = first_commit_time("rounds/round-0-by-hand/REQUEST.md", cwd)
    prod = [p for p in ["identity.md", "rules.md", "examples.md", "reference"] if os.path.exists(os.path.join(cwd, p))]
    for p in prod:
        t, h = first_commit_time(p, cwd)
        ok = req[0] is not None and t is not None and req[0] < t
        res.append((f"(i) round-0 REQUEST ({req[1]}) before first commit of {p} ({h})", ok))
    if os.path.exists(os.path.join(cwd, "examples.md")):
        ex_t, ex_h = first_commit_time("examples.md", cwd)
        for p in ["expected", "fixtures"]:  # the predictions and the inputs are committed before the first report
            t, h = first_commit_time(p, cwd)
            res.append((f"(i) {p}/ ({h}) before first commit of examples.md ({ex_h})", bool(t and ex_t and t < ex_t)))
    for d in sorted(glob.glob(os.path.join(cwd, "rounds", "control-*")) + glob.glob(os.path.join(cwd, "rounds", "refusal*")) + glob.glob(os.path.join(cwd, "rounds", "walk-*"))):
        if not os.path.isdir(d): continue
        n = os.path.basename(d)
        ex = first_commit_time(os.path.relpath(os.path.join(d, "expected.md"), cwd), cwd)
        tr = first_commit_time(os.path.relpath(os.path.join(d, "transcript.md"), cwd), cwd)
        if ex[0] and tr[0]: res.append((f"(i) {n}: expected ({ex[1]}) before transcript ({tr[1]})", ex[0] < tr[0]))
        elif ex[0]: res.append((f"(i) {n}: expected committed ({ex[1]}), transcript not yet", True))
        else: res.append((f"(i) {n}: expected.md not committed", False))
    rounds = sorted(d for d in glob.glob(os.path.join(cwd, "rounds", "round-*")) if os.path.isdir(d))
    prev = None
    for d in rounds:
        n = os.path.basename(d)
        if n.startswith("round-0"):
            tr = first_commit_time(os.path.relpath(os.path.join(d, "transcript.md"), cwd), cwd)
            if tr[0]: res.append((f"(i) {n}: REQUEST ({req[1]}) before transcript ({tr[1]})", req[0] < tr[0]))
            last = tr[0] or req[0]
        else:
            ex = first_commit_time(os.path.relpath(os.path.join(d, "expected.md"), cwd), cwd)
            tr = first_commit_time(os.path.relpath(os.path.join(d, "transcript.md"), cwd), cwd)
            if ex[0] and tr[0]: res.append((f"(i) {n}: expected ({ex[1]}) before transcript ({tr[1]})", ex[0] < tr[0]))
            elif ex[0] and not tr[0]: res.append((f"(i) {n}: expected committed ({ex[1]}), transcript not yet", True))
            else: res.append((f"(i) {n}: expected.md not committed", False))
            last = tr[0] or ex[0]
        if prev and last: res.append((f"(i) {n} after the previous round", prev <= last))
        prev = last
    return res

def check_remote():
    git("fetch", "-q", "origin")
    head, remote = git("rev-parse", "HEAD"), git("rev-parse", "origin/main")
    dirty = git("status", "--porcelain")
    return [(f"(ii) HEAD == origin/main ({head[:7]} / {remote[:7]})", head == remote),
            ("(ii) working tree clean", dirty == "")]

def check_clone():
    url = git("remote", "get-url", "origin")
    tmp = tempfile.mkdtemp(prefix="nfse-auditor-clone-")
    subprocess.run(["git", "clone", "-q", url, tmp], check=False, capture_output=True)
    if not os.path.exists(os.path.join(tmp, ".git")): return [("(iii) fresh clone", False)]
    res = [("(iii) fresh clone into a new folder: " + tmp, True)]
    res += [(l.replace("(i)", "(iii)/(i)"), ok) for l, ok in check_order(tmp)]
    r = subprocess.run([sys.executable, os.path.join(tmp, "tools", "check_audit.py")], cwd=tmp, capture_output=True, text=True)
    res.append(("(iii) tools/check_audit.py passes in the clone", r.returncode == 0))
    return res

def main():
    verify = "--verify" in sys.argv
    res = ([] if verify else check_order(ROOT)) + check_remote() + check_clone()
    stamp = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [f"# ORDER-PROOF — {stamp} — HEAD {git('rev-parse','--short','HEAD')}" + (" — verify mode (read-only)" if verify else ""), ""]
    lines += [f"- {'PASS' if ok else 'FAIL'}  {l}" for l, ok in res]
    lines += ["", "Commands: git log --diff-filter=A --follow --format='%ct %h' -- <path> · git fetch · git rev-parse HEAD origin/main · git status --porcelain · git clone <origin> <tmp> · python3 tools/check_audit.py (in the clone)"]
    out = "\n".join(lines); print(out)
    if not verify: open(os.path.join(ROOT, "rounds", "ORDER-PROOF.md"), "w").write(out + "\n")
    sys.exit(0 if all(ok for _, ok in res) else 1)

if __name__ == "__main__": main()
