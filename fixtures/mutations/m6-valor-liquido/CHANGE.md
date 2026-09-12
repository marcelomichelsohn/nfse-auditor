# CHANGE — m6-valor-liquido

- **Base:** `fixtures/clean/nfse-01.xml` (a correct note).
- **Field changed (one):** `infNFSe/valores/vLiq` — before `400.00` → after `380.00`.
- **Check that must catch it:** check 5 (`5-aritmética`) — rule: LC116 art. 7. The note has no deduction and no retention, so `vLiq` must equal `vServ` = 400,00; 380,00 does not add up.
- **Why this mutation exists (09/09/2026):** m5 changed `vISSQN`, and the run showed that on a note without a rate field the rule cannot call the ISS value wrong (see `../m5-aritmetica-iss/CHANGE.md` and example 2 of `rounds/fixture-runs-v1/report-all-runs.md` — evidence for the reader, not part of what you load). This one alters the part of check 5 that is always checkable.
- **Expected:** `expected/m6-valor-liquido.md`.
