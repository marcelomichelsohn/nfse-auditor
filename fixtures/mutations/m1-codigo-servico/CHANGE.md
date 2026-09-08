# CHANGE — m1-codigo-servico

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `cTribNac` — before `171901` → after `010101`.
- **Check that must catch it:** check 1 — rule: LC116 list item 17 · LC116 art. 1.
- **Why this mutation:** the code on the note (01.01.01, systems analysis) is not the item the client is registered for (17.19, accounting) — the code exists in ANEXO B, so only the profile comparison catches it.
- **Expected:** `expected/m1-codigo-servico.md`.
