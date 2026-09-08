# expected — m5-aritmetica-iss (mutation of nfse-01: vISSQN 8.00 → 12.00)

**What was fed:** `fixtures/mutations/m5-aritmetica-iss/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m5-aritmetica-iss | 5-aritmética | LC116 art. 7 | FALHA | bloqueia o fechamento | infNFSe/valores/vISSQN = 12.00 (vBC 400.00; 12,00 ≠ 400,00 × 2,00% = 8,00) | A base de cálculo do imposto é o preço do serviço. |
| m5-aritmetica-iss | 5-alíquota | LC123 art. 18 §22-A | NÃO SE APLICA | — | infNFSe/valores/vISSQN = 12.00 (optant, accounting society — fixed ISS) | recolherá o ISS em valor fixo, na forma da legislação municipal. |

Não lidos: —
