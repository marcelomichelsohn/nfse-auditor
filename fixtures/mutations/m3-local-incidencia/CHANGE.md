# CHANGE — m3-local-incidencia

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `cLocIncid` — before `2800308` → after `3550308`.
- **Check that must catch it:** check 3 — rule: LC116 art. 3 · LC116 art. 4.
- **Why this mutation:** the incidence municipality set to São Paulo while the provider is established in Aracaju and item 17.19 is not an art. 3 exception.
- **Expected:** `expected/m3-local-incidencia.md`.
