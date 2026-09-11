# ORDER-PROOF — 2026-09-11T05:55:51-03:00 — HEAD 29f0736

- PASS  (i) round-0 REQUEST (1aa296e) before first commit of identity.md (84bd57a)
- PASS  (i) round-0 REQUEST (1aa296e) before first commit of rules.md (84bd57a)
- PASS  (i) round-0 REQUEST (1aa296e) before first commit of examples.md (2112f77)
- PASS  (i) round-0 REQUEST (1aa296e) before first commit of reference (fd52b9d)
- PASS  (i) expected/ (760eaa0) before first commit of examples.md (2112f77)
- PASS  (i) fixtures/ (760eaa0) before first commit of examples.md (2112f77)
- PASS  (i) control-bare-model: expected committed (0e56d83), transcript not yet
- PASS  (i) control-no-reference: expected (fd3e976) before transcript (5443beb)
- PASS  (i) refusal: expected (fd3e976) before transcript (76dabe2)
- PASS  (i) round-0-by-hand: REQUEST (1aa296e) before transcript (5e829d7)
- PASS  (i) round-1-v1: expected (6182de2) before transcript (739b87a)
- PASS  (i) round-1-v1 after the previous round
- PASS  (ii) HEAD == origin/main (29f0736 / 29f0736)
- PASS  (ii) working tree clean
- PASS  (iii) fresh clone into a new folder: /var/folders/49/dv_17z_s38b6gzqtzgdsd_5c0000gp/T/nfse-auditor-clone-ny11ovz4
- PASS  (iii)/(i) round-0 REQUEST (1aa296e) before first commit of identity.md (84bd57a)
- PASS  (iii)/(i) round-0 REQUEST (1aa296e) before first commit of rules.md (84bd57a)
- PASS  (iii)/(i) round-0 REQUEST (1aa296e) before first commit of examples.md (2112f77)
- PASS  (iii)/(i) round-0 REQUEST (1aa296e) before first commit of reference (fd52b9d)
- PASS  (iii)/(i) expected/ (760eaa0) before first commit of examples.md (2112f77)
- PASS  (iii)/(i) fixtures/ (760eaa0) before first commit of examples.md (2112f77)
- PASS  (iii)/(i) control-bare-model: expected committed (0e56d83), transcript not yet
- PASS  (iii)/(i) control-no-reference: expected (fd3e976) before transcript (5443beb)
- PASS  (iii)/(i) refusal: expected (fd3e976) before transcript (76dabe2)
- PASS  (iii)/(i) round-0-by-hand: REQUEST (1aa296e) before transcript (5e829d7)
- PASS  (iii)/(i) round-1-v1: expected (6182de2) before transcript (739b87a)
- PASS  (iii)/(i) round-1-v1 after the previous round
- PASS  (iii) tools/check_audit.py passes in the clone

Commands: git log --diff-filter=A --follow --format='%ct %h' -- <path> · git fetch · git rev-parse HEAD origin/main · git status --porcelain · git clone <origin> <tmp> · python3 tools/check_audit.py (in the clone)
