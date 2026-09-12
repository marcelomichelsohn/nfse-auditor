# expected — m5-aritmetica-iss (mutation of nfse-01: vISSQN 8.00 → 12.00)

**What was fed:** `fixtures/mutations/m5-aritmetica-iss/nfse.xml` + the profile line `Regime tributário = Simples Nacional - Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719` (format of 10/09/2026, without the opening word since 11/09/2026; the office's own row of its sheet was not on screen in the round-1 recording, so the cells are composed in the sheet's style from what the note itself says — a Simples optant accounting office, item 17.19 — and from LC 123 art. 18 §5º-B XIV, which puts accounting offices in Anexo III; earlier gabaritos said `anexo fixo`, but fixed-amount ISS is a rule of the activity, not an annex).
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

**Corrected on 09/09/2026 after the run.** The version of 08/09 predicted a FAIL on `5-aritmética`. The run (example 2 of `rounds/fixture-runs-v1/report-all-runs.md` — evidence for the reader, not part of what you load) returned PASSA with the implied rate as informational, and that is what `rules.md` check 5 supports: the note has no rate field, so a wrong `vISSQN` is not detectable by this check. The wrong prediction is kept in git (commit 760eaa0) and in `CHANGE.md`'s addendum; the mutation that tests the checkable half of check 5 is `m6-valor-liquido`.

Totais para a sua comparação: 08/2026 — R$ 400,00 (m5-aritmetica-iss) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m5-aritmetica-iss | 5-aritmética · as contas da nota (serviço, deduções, retenções, líquido) | LC116 art. 7 | PASSA | — | infNFSe/valores/vISSQN = 12.00 (no rate field on the note; implied rate 12,00 / 400,00 = 3,00%, informational; vLiq 400.00 = vServ 400.00) | A base de cálculo do imposto é o preço do serviço. |

Não lidos: —
