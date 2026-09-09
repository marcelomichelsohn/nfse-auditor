# expected — m5-aritmetica-iss (mutation of nfse-01: vISSQN 8.00 → 12.00)

**What was fed:** `fixtures/mutations/m5-aritmetica-iss/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`.

**Corrected on 09/09/2026 after the run.** The version of 08/09 predicted a FAIL on `5-aritmética`. The run (example 2 of `examples.md`) returned PASSA with the implied rate as informational, and that is what `rules.md` check 5 supports: the note has no rate field, so a wrong `vISSQN` is not detectable by this check. The wrong prediction is kept in git (commit 760eaa0) and in `CHANGE.md`'s addendum; the mutation that tests the checkable half of check 5 is `m6-valor-liquido`.

Totais para a sua comparação: 08/2026 — R$ 400,00 (m5-aritmetica-iss) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m5-aritmetica-iss | 5-aritmética | LC116 art. 7 | PASSA | — | infNFSe/valores/vISSQN = 12.00 (no rate field on the note; implied rate 12,00 / 400,00 = 3,00%, informational; vLiq 400.00 = vServ 400.00) | A base de cálculo do imposto é o preço do serviço. |

Não lidos: —
