# expected — m1-rephrase-a (the m1 violation, description reworded — variant a)

**What was fed:** `fixtures/rephrase/m1-rephrase-a.xml` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`, in a conversation of its own.
**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. Rows not listed here are as in `expected/nfse-01.md`.

Totais para a sua comparação: 08/2026 — R$ 400,00 (m1-rephrase-a) — per note fed.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| m1-rephrase-a | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 list item 17 | FALHA | corrigir antes de fechar · você decide antes de fechar | DPS/infDPS/serv/cServ/cTribNac = 010101 (profile: item 17.19) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| m1-rephrase-a | 1-descrição · descrição escrita pelo cliente comparada com a descrição oficial do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | DPS/infDPS/serv/cServ/xDescServ = "Honorários contábeis referentes ao mês de agosto de 2026." | tem como fato gerador a prestação de serviços constantes da lista anexa |

Não lidos: —
