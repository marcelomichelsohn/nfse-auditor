# expected — m6-valor-liquido (mutation of nfse-01: vLiq 400.00 → 380.00)

**What was fed:** `fixtures/mutations/m6-valor-liquido/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. Rows not listed here are as in `expected/nfse-01.md`. Written 09/09/2026, before the run. **Severity corrected after the run** (author's label "3a"): the prediction said `bloqueia o fechamento`; the auditor said `corrigir antes de fechar`, and `rules.md` § 3 supports it — a wrong net value does not change the tax. The earlier version is in git (commit 08876fc).

Totais para a sua comparação: 08/2026 — R$ 400,00 (m6-valor-liquido) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m6-valor-liquido | 5-aritmética | LC116 art. 7 | FALHA | corrigir antes de fechar | infNFSe/valores/vLiq = 380.00 (vServ 400.00 − 0,00 deductions − 0,00 retentions = 400.00) | A base de cálculo do imposto é o preço do serviço. |

Não lidos: —
