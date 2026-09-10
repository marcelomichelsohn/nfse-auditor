# expected — m1-codigo-servico (mutation of nfse-01: cTribNac 171901 → 010101)

**What was fed:** `fixtures/mutations/m1-codigo-servico/nfse.xml` + the profile line `perfil: Regime tributário = Simples Nacional - Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719` (format of 10/09/2026; the office's own row of its sheet was not on screen in the round-1 recording, so the cells are composed in the sheet's style from what the note itself says — a Simples optant accounting office, item 17.19 — and from LC 123 art. 18 §5º-B XIV, which puts accounting offices in Anexo III; earlier gabaritos said `anexo fixo`, but fixed-amount ISS is a rule of the activity, not an annex).
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m1-codigo-servico | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 list item 17 | FALHA | corrigir antes de fechar · você decide antes de fechar | DPS/infDPS/serv/cServ/cTribNac = 010101 (profile: item 17.19) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| m1-codigo-servico | 1-descrição · descrição escrita pelo cliente comparada com a descrição oficial do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 …" | tem como fato gerador a prestação de serviços constantes da lista anexa |

Não lidos: —
