# CHANGE — m5-aritmetica-iss

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `vISSQN` — before `8.00` → after `12.00`.
- **Check that must catch it:** check 5 — rule: LC116 art. 7.
- **Why this mutation:** the ISS value no longer equals base × the rate implied by the rest of the note (400,00 × 2% = 8,00); the arithmetic row must fail regardless of the rate table not applying.
- **Expected:** `expected/m5-aritmetica-iss.md`.
