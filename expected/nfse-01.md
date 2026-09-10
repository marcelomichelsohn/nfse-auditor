# expected — nfse-01 (clean, the office → the author's company, 02/09/2026)

**What was fed:** `fixtures/clean/nfse-01.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 list item 17 | PASSA | — | DPS/infDPS/serv/cServ/cTribNac = 171901 | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| nfse-01.xml | 1-descrição · descrição escrita pelo cliente comparada com a descrição oficial do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 …" | tem como fato gerador a prestação de serviços constantes da lista anexa |
| nfse-01.xml | 2 · campos obrigatórios do leiaute nacional | NFSe/infNFSe/DPS/infDPS/dCompet | PASSA | — | DPS/infDPS/dCompet = 2026-08-31 | — |
| nfse-01.xml | 3 · município onde o ISS é devido | LC116 art. 3 | PASSA | — | infNFSe/cLocIncid = 2800308 (= cLocEmi 2800308; item 17.19 not in art. 3 I–XXV) | O serviço considera-se prestado e o imposto devido no local do estabelecimento prestador |
| nfse-01.xml | 4 · marcações do Simples Nacional comparadas com o regime do cadastro | LC123 art. 13 | PASSA | — | DPS/infDPS/prest/regTrib/opSimpNac = 3 (regApTribSN = 1; tribISSQN = 1; tpRetISSQN = 1; profile: optante) | VIII - Imposto sobre Serviços de Qualquer Natureza |
| nfse-01.xml | 5-aritmética · as contas da nota (serviço, deduções, retenções, líquido) | LC116 art. 7 | PASSA | — | infNFSe/valores/vISSQN = 8.00 (no rate field on the note; implied rate vISSQN/vBC = 8,00/400,00 = 2,00%, informational, this note's own number; vLiq 400.00 = vServ) | A base de cálculo do imposto é o preço do serviço. |
| nfse-01.xml | 5-alíquota · alíquota de ISS que a nota mostra | LC123 art. 18 §22-A | NÃO SE APLICA | — | infNFSe/valores/vISSQN = 8.00 (implied 2,00% on this note; the municipal table does not apply: optant — ISS inside the DAS; accounting society — fixed amount) | recolherá o ISS em valor fixo, na forma da legislação municipal. |
| nfse-01.xml | 6 · IBS e CBS | RFB 2026 — Orientações | NÃO SE APLICA | — | (no CST/cClassTrib on the note; no municipality of the portfolio exposes the fields) | Emitir documentos fiscais eletrônicos com destaque da CBS e do IBS, individualizados por operação |

Não lidos: —
