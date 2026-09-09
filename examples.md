# examples.md — worked audits, exactly as the auditor returned them

These are real runs of this folder in a Claude project, on the fixtures in `fixtures/` (anonymised notes of the author's own company, issued by the office), kept **verbatim** — nothing was corrected after the run. Each example says what was fed and in what conditions; the expected result of each run, written before the run, is in `expected/` (outside the loaded set). Each Portuguese report is followed by its English twin, produced by the auditor in the same conversation on the request "Please repeat the report above in English": the English quotes are looked up in `reference/en/`, never translated by the model.

## Example 1 — a correct note (nfse-01), with the profile line

**What was fed:** `fixtures/clean/nfse-01.xml` (attached) + the line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**Conditions:** Claude desktop app, a project with the files `CLAUDE.md` lists except `README.md` and `examples.md` (neither existed yet in usable form); model Claude Opus 4.8, effort "low"; 2026-09-09 09:50; operator: the author. Expected result: `expected/nfse-01.md`.

### Report (Portuguese, verbatim)

**Totais para a sua comparação:** competência 08/2026 (dCompet 2026-08-31) → soma de `vServ` = **R$ 400,00** (1 nota lida).

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-código | LC116 list item 17 | PASSA | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (item 17.19; perfil `item LC 116 = 17.19`; código consta na ANEXO_B) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| nfse-01.xml | 1-descrição | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | `xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares."` × `DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 ..."` — coincidência entre o texto livre e o código é juízo, não mecânica | A incidência do imposto não depende da denominação dada ao serviço prestado. |
| nfse-01.xml | 2 | required-fields.md (ANEXO I / XSD v1.01) | PASSA | — | Todos os obrigatórios da trilha usada presentes e não vazios (ex.: `DPS/infDPS/valores/vServPrest/vServ = 400.00`; `infNFSe/valores/vLiq = 400.00`); grupos em `choice` satisfeitos (CNPJ no emit/prest/toma; endNac; cLocPrestacao) | Valor líquido da NFS-e. |
| nfse-01.xml | 3 | LC116 art. 3 | PASSA | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`; item 17.19 não está nas exceções I–XXV | O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador |
| nfse-01.xml | 4 | LC123 art. 13 | PASSA | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optante) coerente com perfil `regime = Simples optante`; `regApTribSN = 1`; `valores/trib/tribMun/tribISSQN = 1`; `tpRetISSQN = 1` (não retido) — coerentes entre si | mediante documento único de arrecadação, |
| nfse-01.xml | 5-aritmética | LC116 art. 7 | PASSA | — | `vLiq 400.00` = `vServ 400.00` − 0,00 (deduções) − 0,00 (retenções); `vISSQN 8.00` / `vBC 400.00` | A base de cálculo do imposto é o preço do serviço. |
| nfse-01.xml | 5-alíquota | LC123 art. 13 | NÃO SE APLICA | — | Sem campo `pAliqAplic`; alíquota implícita `vISSQN/vBC = 8,00/400,00 = 2,00%` (xOutInf: "2,0000%"). Para optante do Simples a tabela municipal de alíquotas não é a aplicável (ISS no DAS; contador em valor fixo) | mediante documento único de arrecadação, |
| nfse-01.xml | 6 | LC214 art. 62 | NÃO SE APLICA | — | Nesta versão sempre NÃO SE APLICA: a nota não traz grupo `IBSCBS`/`CST`/`cClassTrib`; exposição de IBS/CBS nos DF-e passa a ser exigida conforme as notas técnicas a partir de 01/01/2026 | os Municípios e o Distrito Federal ficam obrigados, a partir de 1º de janeiro de 2026 |

**Não lidos:** (nenhum) — o arquivo é XML NFS-e de padrão nacional (raiz `NFSe` v1.01 com `DPS` embutido) e foi auditado.

### The same report in English (verbatim). Not a new audit: the second message of the same conversation asked for the report above in English. What it shows is that the English quotes were looked up in `reference/en/`, not translated. (`rules.md` was updated between the two messages — commit 72ed913 — but no audit was re-run.)

**Totals for your comparison:** competency 08/2026 (dCompet 2026-08-31) → sum of `vServ` = **R$ 400.00** (1 note read).

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-code | LC116 list item 17 | PASS | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (item 17.19; profile `item LC 116 = 17.19`; code exists in ANEXO_B) | 17.19 – Accounting, including technical and auxiliary services. |
| nfse-01.xml | 1-description | LC116 art. 1 | CANNOT DETERMINE | — | `xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares."` × `DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 ..."` — whether the free text matches the code is a judgement | The levy of the tax does not depend on the name given to the service rendered. |
| nfse-01.xml | 2 | required-fields.md (ANEXO I / XSD v1.01) | PASS | — | All required fields on the used path present and non-empty (e.g. `DPS/infDPS/valores/vServPrest/vServ = 400.00`; `infNFSe/valores/vLiq = 400.00`); every `choice` group satisfied (CNPJ in emit/prest/toma; endNac; cLocPrestacao) | Valor líquido da NFS-e. |
| nfse-01.xml | 3 | LC116 art. 3 | PASS | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`; item 17.19 is not among the exceptions I–XXV | The service is considered rendered, and the tax, due, at the location of the provider's establishment |
| nfse-01.xml | 4 | LC123 art. 13 | PASS | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optant) coherent with profile `regime = Simples optante`; `regApTribSN = 1`; `valores/trib/tribMun/tribISSQN = 1`; `tpRetISSQN = 1` (not withheld) — coherent among themselves | entails the monthly collection, by means of a single collection document, |
| nfse-01.xml | 5-arithmetic | LC116 art. 7 | PASS | — | `vLiq 400.00` = `vServ 400.00` − 0.00 (deductions) − 0.00 (retentions); `vISSQN 8.00` / `vBC 400.00` | The tax base is the price of the service. |
| nfse-01.xml | 5-rate | LC123 art. 13 | NOT APPLICABLE | — | No `pAliqAplic` field; implied rate `vISSQN/vBC = 8.00/400.00 = 2.00%` (xOutInf: "2,0000%"). For a Simples optant the municipal rate table is not the applicable rate (ISS inside the DAS; accountant at a fixed amount) | entails the monthly collection, by means of a single collection document, |
| nfse-01.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | Always NOT APPLICABLE in this version: the note carries no `IBSCBS`/`CST`/`cClassTrib` group; IBS/CBS exposure on DF-e becomes required per the technical notes from 01/01/2026 | the Municipalities and the Federal District are required, as of January 1, 2026 |

**Not read:** (none) — the file is a national-standard NFS-e XML (root `NFSe` v1.01 with embedded `DPS`) and was audited.
