# Control — the same note, the folder loaded WITHOUT `reference/` — expected (written 09/09/2026, before the run)

**Why this run exists.** Everything the auditor cites must come from `reference/`. This control removes `reference/` and feeds the same note, so a reader can see what the model does when the standard is not in the folder: the quotes it produces are from memory, and `tools/check_audit.py` C1 must fail to resolve them. It is the same idea as a control in an experiment: it shows that the folder, not the model's memory, is what makes a report checkable.

**What is loaded in the control project:** `identity.md`, `rules.md`, `README.md`, the entry file `CLAUDE.md` (as project instructions). **Not loaded:** `reference/` (nothing of it), `examples.md`.
**What is fed:** `fixtures/clean/nfse-01.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.

**Prediction.**
1. The model still produces the table of `rules.md` § 3.
2. In the column "trecho citado", some or all quotes will not be verbatim substrings of `reference/pt/`: C1 run on `transcript.md` reports unresolved rows. The count is the measure; it is written in `what-this-shows.md` after the run, from the checker's output, never typed by hand.
3. Some provision ids may be wrong or invented (an article number the standard does not have) — C2 catches an id that is not in `reference/INDEX.md`.

**What this control does not prove.** One note, one run, one model. It does not prove that the runs with `reference/` loaded are correct — `expected/` and the rounds do that. It only shows that without the standard in the folder the report cannot be checked, which is the brief's own test.
