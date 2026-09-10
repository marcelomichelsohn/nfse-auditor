# expected — m1-codigo-servico (mutation of nfse-01: cTribNac 171901 → 010101)

**What was fed:** `fixtures/mutations/m1-codigo-servico/nfse.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report (`rules.md` § 3, 10/09/2026) repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 400,00 (nfse-01) · 09/2026 — R$ 400,00 (nfse-02) — per note fed.

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m1-codigo-servico | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 list item 17 | FALHA | corrigir antes de fechar · você decide antes de fechar | DPS/infDPS/serv/cServ/cTribNac = 010101 (profile: item 17.19) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| m1-codigo-servico | 1-descrição · descrição escrita pelo cliente comparada com a descrição oficial do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 …" | tem como fato gerador a prestação de serviços constantes da lista anexa |

Não lidos: —
