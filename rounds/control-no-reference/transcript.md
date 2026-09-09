# Control — the folder loaded WITHOUT `reference/` — transcript (2026-09-09, ~12:55; the operator is the author)

**Set-up:** a second Claude project with the same entry file as instructions and **only** `identity.md` and `rules.md` uploaded (`rules.md` at commit f38ec00); no `reference/`, no `examples.md`, no README. One conversation: `fixtures/clean/nfse-01.xml` attached + the profile line. Claude Opus 4.8, effort "low". Prediction: `expected.md` (committed before the run). What this shows, measured by the checker: `what-this-shows.md`.
**Kept as it came.** The answer is verbatim; the operator is addressed by the role label of `rounds/README.md`.

---

**Operator:** *(attaches `nfse-01.xml` + the profile line)*

**Auditor:**

Marcelo — antes da tabela, um aviso que muda como você lê o resultado: **neste projeto só estão carregados `identity.md` e `rules.md`.** O corpus `reference/` (INDEX, excerpts, ANEXO A/B, `required-fields.md`, CSVs municipais/working) e o `examples.md` não estão no mount. Procurei no filesystem inteiro — não existem aqui.

Consequência direta pelas próprias regras do auditor:

- A coluna **`trecho citado`** exige texto **verbatim** de `reference/pt/excerpts/`, "nunca parafraseado, nunca traduzido por você" (rules.md §3) — e identity.md proíbe inventar citação. Sem os excerpts, **não preencho essa coluna** (não vou fabricar o texto legal).
- **Check 1-código** (existência de `171901` no ANEXO B) e **Check 2** (campos obrigatórios vs. `required-fields.md`) dependem de tabelas que não estão carregadas → ficam **NÃO DÁ PARA DETERMINAR** por falta de corpus, não por falta de dado na nota.
- **`dispositivo`** deveria vir do "Cite as" de `reference/INDEX.md`; uso abaixo o rótulo da provisão como aparece em rules.md e sinalizo que o id exato depende do INDEX.

O que **consigo** determinar com segurança a partir do XML + linha de perfil roda normalmente. Segue o que dá, marcado honestamente.

**Totais para a sua comparação:** 2026-08 (dCompet 2026-08-31) → **R$ 400,00** (1 nota lida).

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-código | LC116 art. 1 · item 17.19 | NÃO DÁ PARA DETERMINAR | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` | *(corpus não carregado — ANEXO B ausente; item do código = 17.19, **igual** ao perfil, mas não confirmo existência do código sem a tabela)* |
| nfse-01.xml | 1-descrição | LC116 list item 17 | NÃO DÁ PARA DETERMINAR | — | `xDescServ = "1 Investimento Contábil. 400,00…"` vs `xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares."` | *(juízo sobre palavras — CANNOT DETERMINE por desenho)* |
| nfse-01.xml | 2 | ANEXO I / XSD v1.01 | NÃO DÁ PARA DETERMINAR | — | nota populada e bem-formada na inspeção manual | *(corpus não carregado — `required-fields.md` ausente; não confirmo a lista de obrigatórios)* |
| nfse-01.xml | 3 | LC116 art. 3 · art. 4 | PASSA | — | `cLocIncid = 2800308` (Aracaju) = `cLocEmi = 2800308`; item 17.19 fora das exceções do art. 3 | *(corpus não carregado)* |
| nfse-01.xml | 4 | LC123 art. 18 §22-A · DL406 art. 9 | PASSA | — | `prest/regTrib/opSimpNac = 3` (optante ME/EPP) coerente com perfil "Simples optante"; `regApTribSN = 1`; `tribISSQN = 1`; `tpRetISSQN = 1` | *(corpus não carregado)* |
| nfse-01.xml | 5-aritmética | LC116 art. 7 | PASSA | — | `vLiq = 400,00` = `vServ 400,00` − 0 deduções − 0 retenções (`tpRetISSQN=1`) | *(corpus não carregado)* |
| nfse-01.xml | 5-alíquota | LC123 art. 13 · art. 18 §22-A · DL406 art. 9 | NÃO SE APLICA | — | optante do Simples, anexo fixo (soc. contábil); ISS não pela tabela municipal. Alíquota implícita `vISSQN 8,00 / vBC 400,00 = 2,0%` — informativa, não é FALHA | *(corpus não carregado)* |
| nfse-01.xml | 6 | LC214 art. 62 | NÃO SE APLICA | — | nota sem `CST`/`cClassTrib` | *(corpus não carregado)* |

**Não lidos:** nenhum. O arquivo é NFS-e XML do padrão nacional (`NFSe` versao 1.01 com `DPS` embutido).

Uma nota de conteúdo, separada do resultado acima: a única coisa que me chamou atenção na inspeção manual é `tpRetISSQN = 1` (não retido) convivendo com `xDescServ` começando em "**1 Investimento Contábil**" — divergência descrição×código que é exatamente o que 1-descrição devolve como indeterminável. Não é achado; é o motivo de a linha existir.

Se quiser a tabela **completa e citável** (coluna `trecho citado` verbatim, existência em ANEXO B, check 2 real), o caminho é carregar o `reference/` no projeto. Quer que eu rode de novo assim que subir o corpus, ou prefere que eu detalhe agora qual subconjunto mínimo de arquivos destrava cada check?
