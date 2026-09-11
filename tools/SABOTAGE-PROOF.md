# SABOTAGE-PROOF — 2026-09-11T17:42:22-03:00 — HEAD b2cd9d2

Each line: a claim of `tools/README.md`, its sabotage applied to a fresh scratch copy, and the first line the command printed. CAUGHT = the command failed, as the claim says it must.

- CAUGHT  quotes verbatim (C1) — `FAIL C1  expected/nfse-01.md:10: quote does not resolve in reference/pt/: “17.19 – Contebilidade, inclusive serviços técnicos e auxilia…”`
- CAUGHT  excerpts cut from the full texts (C0) — `FAIL C0  reference/pt/excerpts/dl406_art9.txt: excerpt is not a verbatim substring of any full text`
- CAUGHT  a mutation's prediction FAILS on its check (C3) — `FAIL C3  expected/m2-campo-obrigatorio.md: no FAIL row for check 2 named in CHANGE.md`
- CAUGHT  one prediction per fixture, rephrase included (C3) — `FAIL C3  fixtures/rephrase/m1-rephrase-b.xml: expected/m1-rephrase-b.md: found 0, need exactly 1`
- CAUGHT  the README's load list never names the evidence (C5) — `FAIL C5  README.md: load list names fixtures/`
- CAUGHT  the entry file only routes (C5) — `FAIL C5  CLAUDE.md: entry file carries content ('PASSA'); rules live in rules.md`
- CAUGHT  make_load_folder refuses an evidence path — `FAIL these paths are evidence, never loaded (README.md § What to load): ['fixtures/clean/nfse-01.xml']`
- CAUGHT  the committed zip is the current files (--check) — `FAIL the zip in download/ differs from the current files (rebuild: python3 tools/make_load_folder.py download): ['identity.md']`
- CAUGHT  no real identifier (C6) — `FAIL C6  rules.md:76: check-digit-valid CNPJ in text: [the planted CNPJ]`
- CAUGHT  predictions before reports, from git (prove_order) — `(i) round-9-sabotage: expected (83ed090) before transcript (72e30e7)`
- CAUGHT  the checker is not decoration (--selftest) — `SELFTEST FAIL`
