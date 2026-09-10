# expected — m6-valor-liquido (mutation of nfse-01: vLiq 400.00 → 380.00)

**What was fed:** `fixtures/mutations/m6-valor-liquido/nfse.xml` + the profile line `perfil: Regime tributário = Simples Nacional - Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719` (format of 10/09/2026; the office's own row of its sheet was not on screen in the round-1 recording, so the cells are composed in the sheet's style from what the note itself says — a Simples optant accounting office, item 17.19 — and from LC 123 art. 18 §5º-B XIV, which puts accounting offices in Anexo III; earlier gabaritos said `anexo fixo`, but fixed-amount ISS is a rule of the activity, not an annex).
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape. Rows not listed here are as in `expected/nfse-01.md`. Written 09/09/2026, before the run. **Severity corrected after the run** (author's label "3a"): the prediction said `bloqueia o fechamento`; the auditor said `corrigir antes de fechar`, and `rules.md` § 3 supports it — a wrong net value does not change the tax. The earlier version is in git (commit 08876fc).

Totais para a sua comparação: 08/2026 — R$ 400,00 (m6-valor-liquido) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m6-valor-liquido | 5-aritmética · as contas da nota (serviço, deduções, retenções, líquido) | LC116 art. 7 | FALHA | corrigir antes de fechar · o cliente reemite a nota | infNFSe/valores/vLiq = 380.00 (vServ 400.00 − 0,00 deductions − 0,00 retentions = 400.00) | A base de cálculo do imposto é o preço do serviço. |

Não lidos: —
