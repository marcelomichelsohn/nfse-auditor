# expected — m3-local-incidencia (mutation of nfse-01: cLocIncid 2800308 → 3550308)

**What was fed:** `fixtures/mutations/m3-local-incidencia/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m3-local-incidencia | 3 · município onde o ISS é devido | LC116 art. 3 | FALHA | bloqueia o fechamento · o cliente reemite a nota | infNFSe/cLocIncid = 3550308 (cLocEmi 2800308; item 17.19 not in art. 3 I–XXV) | O serviço considera-se prestado e o imposto devido no local do estabelecimento prestador |

Não lidos: —
