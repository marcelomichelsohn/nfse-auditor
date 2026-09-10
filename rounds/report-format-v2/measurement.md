# measurement — the four report-format variants, measured

> Snapshot of the study (10/09/2026). The labels and the column header `check` in this file are the ones the decision was made on; after it, `rules.md` § 3 reworded three labels and made the Portuguese header `verificação`. The vocabulary that governs is `rules.md`; this file is evidence of the choice, kept as it was.

Measurement only, no recommendation: row widths, where each row runs past 100/120/160 characters, the largest cell per column, and what each variant costs in `tools/check_audit.py`, in `expected/` and in `examples.md`.
Re-run: `python3 rounds/report-format-v2/measure.py` from the repo root (stdlib only; it imports `tools/check_audit.py` and runs C1/C2 over each variant). File counts: `ls expected | wc -l`, `grep -l '^| nota | check' expected/*.md | wc -l`, `grep -c '^| nota | check' examples.md`, `grep -c '^| note | check' examples.md`.

## Summary

| variant | max width | mean width | first 4 cols, max | checker lines to change | C1/C2 findings today | files to change |
|---|---|---|---|---|---|---|
| V0-as-is | 718 | 524.9 | 78 | 0 | 0 | 0 |
| V1-enriched | 796 | 576.9 | 152 | 1 (l.116, or the `SEVER` set at l.33–34) | 1 | 13 (12 `expected/*.md` + `examples.md`) |
| V2-enriched-reordered | 796 | 576.9 | 160 | 2 (l.71 + l.116) | 24 | 13 (12 `expected/*.md` + `examples.md`) |
| V3-enriched-short-location | 313 | 224.6 | 152 | 1 (l.116, or the `SEVER` set at l.33–34) | 1 | 13 (12 `expected/*.md` + `examples.md`) |

Widths are characters (not bytes), over the 8 data rows only (header and separator excluded). "First 4 cols" = from the start of the line to the closing `|` of the 4th cell, inclusive. Mean of the first four columns: V0 62.6 · V1 110.9 · V2 102.6 · V3 110.9.

A prerequisite common to all four, counted in no row above: today `main` reads no variant at all. Line 254 selects report files with `glob("rounds/**/*.md")` filtered by `os.path.basename(p).startswith("transcript") or "report" in os.path.basename(p)` — the basenames here are `V0-as-is.md` … `V3-enriched-short-location.md`, so none match (the folder name `report-format-v2` is not the basename). For any variant to be gated at all, l.254 has to change too. The findings below come from running C1/C2 on each file directly, as `main` would if it selected them.

---

## V0-as-is.md

### Where the cumulative width passes each threshold

| row (check) | >100 | >120 | >160 |
|---|---|---|---|
| 1-código | localização | localização | localização |
| 1-descrição | localização | localização | localização |
| 2 | localização | localização | localização |
| 3 | localização | localização | localização |
| 4 | localização | localização | localização |
| 5-aritmética | localização | localização | localização |
| 5-alíquota | localização | localização | localização |
| 6 | localização | localização | localização |

### Largest cell per column

| column | characters |
|---|---|
| nota | 19 |
| check | 12 |
| dispositivo | 40 |
| resultado | 22 |
| severidade | 24 |
| localização | 607 |
| trecho citado | 91 |

---

## V1-enriched.md

### Where the cumulative width passes each threshold

| row (check) | >100 | >120 | >160 |
|---|---|---|---|
| 1-código | dispositivo | severidade | severidade |
| 1-descrição | check | dispositivo | localização |
| 2 | dispositivo | severidade | localização |
| 3 | localização | localização | localização |
| 4 | dispositivo | severidade | localização |
| 5-aritmética | dispositivo | resultado | localização |
| 5-alíquota | resultado | localização | localização |
| 6 | localização | localização | localização |

### Largest cell per column

| column | characters |
|---|---|
| nota | 19 |
| check | 86 |
| dispositivo | 40 |
| resultado | 22 |
| severidade | 54 |
| localização | 607 |
| trecho citado | 91 |

---

## V2-enriched-reordered.md

### Where the cumulative width passes each threshold

| row (check) | >100 | >120 | >160 |
|---|---|---|---|
| 1-código | resultado | severidade | dispositivo |
| 1-descrição | check | resultado | localização |
| 2 | dispositivo | dispositivo | localização |
| 3 | localização | localização | localização |
| 4 | resultado | dispositivo | localização |
| 5-aritmética | resultado | dispositivo | localização |
| 5-alíquota | dispositivo | localização | localização |
| 6 | localização | localização | localização |

### Largest cell per column

| column | characters |
|---|---|
| nota | 19 |
| check | 86 |
| resultado | 22 |
| severidade | 54 |
| dispositivo | 40 |
| localização | 607 |
| trecho citado | 91 |

---

## V3-enriched-short-location.md

### Where the cumulative width passes each threshold

| row (check) | >100 | >120 | >160 |
|---|---|---|---|
| 1-código | dispositivo | severidade | severidade |
| 1-descrição | check | dispositivo | localização |
| 2 | dispositivo | severidade | trecho citado |
| 3 | localização | localização | trecho citado |
| 4 | dispositivo | severidade | trecho citado |
| 5-aritmética | dispositivo | resultado | trecho citado |
| 5-alíquota | resultado | localização | trecho citado |
| 6 | localização | trecho citado | trecho citado |

### Largest cell per column

| column | characters |
|---|---|
| nota | 19 |
| check | 86 |
| dispositivo | 40 |
| resultado | 22 |
| severidade | 54 |
| localização | 75 |
| trecho citado | 91 |

---

## Cost in `tools/check_audit.py`

The whole file was read (274 lines). What each cited line does, verified in the code, not assumed:

- **l.71** — `ROW` is one regex with seven named groups in fixed order: `nota`, `check`, `disp`, `res`, `sev`, `loc`, `trecho`. Position is the only thing that binds a cell to a name; the header row is never consulted.
- **l.85** (not l.79 — l.79 is the `kept-as-came:end` fence) — `if not re.match(r"^\d", d["check"]): continue`. The check cell only has to *start* with a digit. `1-código · código de serviço da nota comparado com o item do cadastro` still starts with `1`, so **no variant loses rows here**: the checker sees 8 rows in all four (printed by `measure.py`).
- **l.112** — the layout corpus is added when `d["check"].strip().startswith("2")`. `2 · campos obrigatórios do leiaute nacional` still starts with `2`, so the check-2 quote (`Valor líquido da NFS-e.`) still resolves in `reference/tables/required-fields.md` in V1, V2 and V3. **No change needed.**
- **l.115 / l.116** — `d["res"] not in RESULTS` and `d["sev"] not in SEVER`: exact set membership (sets defined l.31 and l.33–34). No prefix, no split, no normalisation.
- **l.118** — the provision cell must be in `reference/INDEX.md` or start with `NFSe/`, `required-fields`, `reference/tables/required-fields` or `ANEXO`.
- **l.146** — C3's regex `\|\s*<digit>(-[\wáéíóúãõç]+)?\s*\|[^|]*\|\s*(FALHA|FAIL)\s*\|` requires the check cell to end right after the optional `-suffix`, and expects exactly one cell between check and result. It is reached only from l.142/l.144, which build the path `expected/<mutation slug>.md`. **It does not bite any variant** — no variant file is ever passed to C3. It bites the moment the variant's shape is propagated into `expected/`, which is what the "files to change" column counts.

### V0-as-is — 0 lines

C1/C2 findings: 0. Nothing in the checker has to change.

### V1-enriched — 1 line

C1/C2 findings: 1, all of it the severity cell.

- **l.116** — today `d["sev"] not in SEVER` rejects `corrigir antes de fechar · você decide antes de fechar`. It would have to compare only the part before ` · ` (e.g. `d["sev"].split(" · ")[0]`), so the gloss is carried but not gated.
- Equivalent single-site alternative: **l.33–34**, adding the glossed strings to `SEVER` verbatim — cheaper to write, but it freezes the gloss's wording inside the checker.
- The check-cell gloss costs nothing: l.85 and l.112 both only look at the first character(s).

### V2-enriched-reordered — 2 lines

C1/C2 findings: 24 — three per row across all eight rows, and every one of them is the same cause: the columns moved and l.71 did not.

- **l.71** — the named groups would have to be reordered to `nota, check, res, sev, disp, loc, trecho`. Today `disp` reads the result cell (`FALHA`, `PASSA` → "provision id not in reference/INDEX.md"), `res` reads the severity cell (`—` → "result word not allowed"), `sev` reads the provision cell (`LC116 art. 1` → "severity not allowed"). Note `loc` and `trecho` stay in place, which is why C1 raises nothing.
- **l.116** — same severity gloss as V1, and it survives the reorder: even with l.71 fixed, `corrigir antes de fechar · você decide antes de fechar` still fails.
- Not a third line, but the consequence to state: l.71 is global. Reordering it makes **every** other report in the repo — `examples.md`, all `expected/*.md`, every `rounds/**/transcript.md`, both `tools/selftest/*.md` — read wrong at once, which is why the file count below is not optional for V2.

### V3-enriched-short-location — 1 line

C1/C2 findings: 1, identical to V1: the severity cell. Same fix, **l.116** (or l.33–34). The short location changes nothing in the checker: l.120's `^([A-Za-z0-9_/\.\-]+)\s*=` still matches, and `find_fixture("nNFSe 2026000000008")` returns `None` for every variant, so the XML-path check at l.126 never runs on these files anyway.

---

## Cost in `expected/` and `examples.md`

`ls expected | wc -l` → **13**. `grep -l '^| nota | check' expected/*.md | wc -l` → **12** carry a report table (37 rows; `not-an-nfse.md` is the 13th and has no table — it predicts *no rows*, so it names no columns and does not move for any variant). `grep -c '^| nota | check' examples.md` → **3** Portuguese tables; `grep -c '^| note | check' examples.md` → **3** English twins; 48 rows in all.

| variant | expected/*.md to change | examples.md | total | what changes in each |
|---|---|---|---|---|
| V0-as-is | 0 | no | **0** | the form is the one already written |
| V1-enriched | 12 | yes | **13** | the check cell of every row gains its gloss (37 + 48 = 85 rows); the 10 non-`—` severity cells (8 in `expected/`, 2 in `examples.md`) gain theirs; the 3 English tables in `examples.md` need English glosses |
| V2-enriched-reordered | 12 | yes | **13** | everything V1 changes, **plus** the header line and all seven cells of every row reordered in all 12 `expected/` tables and all 6 `examples.md` tables |
| V3-enriched-short-location | 12 | yes | **13** | the same gloss edits as V1. The location column needs no shortening: the longest location cell already written is 179 chars in `expected/` and 368 in `examples.md`, both under V0's 607 — but the gabaritos are what a correct audit "must return", so if the short location becomes the rule they are the files that state it |

A knock-on inside the same count, from l.146: the five mutation gabaritos C3 reads by path — `m1-codigo-servico.md`, `m2-campo-obrigatorio.md`, `m3-local-incidencia.md`, `m4-flag-simples.md`, `m6-valor-liquido.md` (`m5-aritmetica-iss.md` is skipped at l.143 by its `**not caught` marker) — must keep matching l.146's regex. Under V1/V3 the glossed check cell no longer ends where l.146 expects; under V2 the result cell is one column earlier. Either way l.146 changes with them; it is listed here rather than in the checker count because it is the gabaritos' shape, not the variant's, that forces it.

---

## Checker output, verbatim

Produced by `python3 rounds/report-format-v2/measure.py`, section 5.

```
==============================================================================
5. CHECKER COST — tools/check_audit.py C1/C2 run over each variant file
==============================================================================

--- V0-as-is.md  (rows the checker sees: 8; findings: 0) ---
    (no C1/C2 findings)

--- V1-enriched.md  (rows the checker sees: 8; findings: 1) ---
    C2  rounds/report-format-v2/V1-enriched.md:7: severity not allowed: 'corrigir antes de fechar · você decide antes de fechar'

--- V2-enriched-reordered.md  (rows the checker sees: 8; findings: 24) ---
    C2  rounds/report-format-v2/V2-enriched-reordered.md:7: result word not allowed: 'corrigir antes de fechar · você decide antes de fechar'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:7: severity not allowed: 'LC116 art. 1'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:7: provision id not in reference/INDEX.md: 'FALHA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:8: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:8: severity not allowed: 'LC116 art. 1'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:8: provision id not in reference/INDEX.md: 'NÃO DÁ PARA DETERMINAR'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:9: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:9: severity not allowed: 'required-fields.md (ANEXO I / XSD v1.01)'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:9: provision id not in reference/INDEX.md: 'PASSA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:10: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:10: severity not allowed: 'LC116 art. 3'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:10: provision id not in reference/INDEX.md: 'PASSA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:11: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:11: severity not allowed: 'LC123 art. 13'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:11: provision id not in reference/INDEX.md: 'PASSA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:12: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:12: severity not allowed: 'LC116 art. 7'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:12: provision id not in reference/INDEX.md: 'PASSA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:13: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:13: severity not allowed: 'LC123 art. 13'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:13: provision id not in reference/INDEX.md: 'NÃO SE APLICA'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:14: result word not allowed: '—'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:14: severity not allowed: 'LC214 art. 62'
    C2  rounds/report-format-v2/V2-enriched-reordered.md:14: provision id not in reference/INDEX.md: 'NÃO SE APLICA'

--- V3-enriched-short-location.md  (rows the checker sees: 8; findings: 1) ---
    C2  rounds/report-format-v2/V3-enriched-short-location.md:7: severity not allowed: 'corrigir antes de fechar · você decide antes de fechar'
```
