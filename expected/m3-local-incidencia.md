# expected — m3-local-incidencia (mutation of nfse-01: cLocIncid 2800308 → 3550308)

**What was fed:** `fixtures/mutations/m3-local-incidencia/nfse.xml` + the profile line `perfil: Regime tributário = Simples Nacional - Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719` (format of 10/09/2026; the office's own row of its sheet was not on screen in the round-1 recording, so the cells are composed in the sheet's style from what the note itself says — a Simples optant accounting office, item 17.19 — and from LC 123 art. 18 §5º-B XIV, which puts accounting offices in Anexo III; earlier gabaritos said `anexo fixo`, but fixed-amount ISS is a rule of the activity, not an annex).
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m3-local-incidencia | 3 · município onde o ISS é devido | LC116 art. 3 | FALHA | bloqueia o fechamento · o cliente reemite a nota | infNFSe/cLocIncid = 3550308 (cLocEmi 2800308; item 17.19 not in art. 3 I–XXV) | O serviço considera-se prestado e o imposto devido no local do estabelecimento prestador |

Não lidos: —
