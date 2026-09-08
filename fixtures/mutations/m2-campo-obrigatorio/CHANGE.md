# CHANGE — m2-campo-obrigatorio

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `dCompet` — before `2026-08-31` → after ``.
- **Check that must catch it:** check 2 — rule: ANEXO I / XSD v1.01 via tables/required-fields.md.
- **Why this mutation:** a required element of the DPS emptied — the layout check must flag the empty required field.
- **Expected:** `expected/m2-campo-obrigatorio.md`.
