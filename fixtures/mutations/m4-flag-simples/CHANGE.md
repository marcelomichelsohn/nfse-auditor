# CHANGE — m4-flag-simples

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `opSimpNac` — before `3` → after `1`.
- **Check that must catch it:** check 4 — rule: LC123 art. 13.
- **Why this mutation:** opSimpNac says "not optant" while regApTribSN (which only exists for optants) is filled and the profile says optant — incoherent among themselves.
- **Expected:** `expected/m4-flag-simples.md`.
