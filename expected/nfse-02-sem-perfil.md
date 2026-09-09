# expected — nfse-02 fed WITHOUT a profile line (the worked null case)

**What was fed:** `fixtures/clean/nfse-02.xml` alone — no profile line. The note is correct; what is missing is the fact the operator supplies.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. Nothing may be guessed from the note: every check that needs the profile returns CANNOT DETERMINE and says so (`rules.md` § 0).

Totais para a sua comparação: 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-02.xml | 1-código | LC116 list item 17 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/cTribNac = 171901 (code exists in ANEXO B; no profile line to compare the item with) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| nfse-02.xml | 1-descrição | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 …" | tem como fato gerador a prestação de serviços constantes da lista anexa |
| nfse-02.xml | 2 | NFSe/infNFSe/DPS/infDPS/dCompet | PASSA | — | DPS/infDPS/dCompet = 2026-09-05 | — |
| nfse-02.xml | 3 | LC116 art. 3 | PASSA | — | infNFSe/cLocIncid = 2800308 (= cLocEmi 2800308; item 17.19 not in art. 3 I–XXV) | O serviço considera-se prestado e o imposto devido no local do estabelecimento prestador |
| nfse-02.xml | 4 | LC123 art. 13 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/prest/regTrib/opSimpNac = 3 (flags coherent among themselves; no profile line to confirm the regime) | VIII - Imposto sobre Serviços de Qualquer Natureza |
| nfse-02.xml | 5-aritmética | LC116 art. 7 | PASSA | — | infNFSe/valores/vISSQN = 8.00 (vBC 400.00 × 2,00% implied; vLiq 400.00 = vServ) | A base de cálculo do imposto é o preço do serviço. |
| nfse-02.xml | 5-alíquota | LC123 art. 18 §22-A | NÃO DÁ PARA DETERMINAR | — | infNFSe/valores/vISSQN = 8.00 (2,00% on the note vs 5% in the municipal table; whether the fixed-amount ISS applies depends on the regime, which the profile line would confirm) | recolherá o ISS em valor fixo, na forma da legislação municipal. |
| nfse-02.xml | 6 | RFB 2026 — Orientações | NÃO SE APLICA | — | (no CST/cClassTrib on the note; no municipality of the portfolio exposes the fields) | Emitir documentos fiscais eletrônicos com destaque da CBS e do IBS, individualizados por operação |

Não lidos: —
