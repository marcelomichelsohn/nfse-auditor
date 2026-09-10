# expected — m4-flag-simples (mutation of nfse-01: opSimpNac 3 → 1)

**What was fed:** `fixtures/mutations/m4-flag-simples/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m4-flag-simples | 4 · marcações do Simples Nacional comparadas com o regime do cadastro | LC123 art. 13 | FALHA | corrigir antes de fechar · você confere o cadastro | DPS/infDPS/prest/regTrib/opSimpNac = 1 (regApTribSN = 1 present; profile: optante) | VIII - Imposto sobre Serviços de Qualquer Natureza |

Não lidos: —
