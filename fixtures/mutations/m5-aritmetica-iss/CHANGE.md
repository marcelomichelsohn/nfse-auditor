# CHANGE — m5-aritmetica-iss

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `vISSQN` — before `8.00` → after `12.00`.
- **Check that must catch it:** check 5 — rule: LC116 art. 7.
- **Why this mutation:** the ISS value no longer equals base × the rate the rest of this note implies (on the clean fixture vISSQN/vBC = 8,00/400,00 = 2,00%; other notes of the office carry other rates — one real note carries 5% — so no rate is a default); the arithmetic row must fail regardless of the rate table not applying.
- **Expected:** `expected/m5-aritmetica-iss.md`.

## Addendum — 09/09/2026, after the run (example 2 of `examples.md`)
**Not caught, and it cannot be, by the rule as written.** The note carries no rate field, so check 5 has nothing to multiply `vBC` by; the rule reports the implied rate (3,00%) as informational, which is what the auditor did. The prediction above ("check 5 must catch it") was wrong. Kept as it was, with this note, so the reader sees the wrong prediction next to the run; `expected/m5-aritmetica-iss.md` was corrected to what the rule supports, and `m6-valor-liquido/` was added to test the checkable half of check 5. Decision: the author, 09/09 ("a").
