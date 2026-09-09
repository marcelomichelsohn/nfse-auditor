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

## Example 2 — a note with one field altered (m5-aritmetica-iss: `vISSQN` 8.00 → 12.00), with the profile line

**What was fed:** `fixtures/mutations/m5-aritmetica-iss/nfse.xml` (attached; the file is named `nfse.xml` inside its folder, which is why the report calls it that) + the same profile line as example 1.
**Conditions:** same project as example 1, `rules.md` at commit 72ed913; model Claude Opus 4.8, effort "low"; 2026-09-09 morning; operator: the author. Expected result, written 08/09 before the run: `expected/m5-aritmetica-iss.md` — a FAIL on `5-aritmética`, severity "bloqueia o fechamento".
**What happened:** the auditor returned PASSA on `5-aritmética` and reported the implied rate (3,00%) as informational. Read against `rules.md` § 2 check 5 as written on 08/09 — "if a rate field is present: vISSQN = vBC × rate; if absent: report the implied rate as informational" — the auditor followed the rule: the note carries no rate field, so the rule had no way to call 12,00 wrong. **The prediction was wrong, not the run.** The report stays as it came; what changed after it is in the commit that follows this one.
The first lines of the answer are the model's own narration of what it opened and ran before the table; they are kept because they are part of what the operator saw.

### Report (Portuguese, verbatim)

Now let me read the uploaded XML note.Now let me read the Portuguese excerpts I'll need to quote verbatim (report defaults to Portuguese).Let me see the remaining required-fields section (infNFSe/valores and DPS tribMun/totTrib children).Now let me mechanically verify Check 2 (mandatory fields) and Check 1 (code in ANEXO B) with a script.Check 2 passes mechanically. Now verifying Check 1 — that cTribNac 171901 exists in ANEXO B and maps to item 17.19.Let me verify each chosen verbatim quote is an exact single-line substring of its excerpt file.Totais para a sua comparação: competência 08/2026 = R$ 400,00 (soma de `vServ`; 1 nota lida)

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | PASSA | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (ANEXO B: item 17, subitem 19 → 17.19); perfil `item LC 116 = 17.19` — coincidem | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| nfse.xml | 1-descrição | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | `xDescServ` = "1 Investimento Contábil. 400,00 … Trib aprox…" × descrição do código 171901 = "Contabilidade, inclusive serviços técnicos e auxiliares." — juízo sobre palavras, não mecânico | A incidência do imposto não depende da denominação dada ao serviço prestado. |
| nfse.xml | 2 | `reference/tables/required-fields.md` (todos os obrigatórios da via usada) | PASSA | — | Todos os elementos `required` do caminho efetivamente usado presentes e não vazios (`emit/enderNac`, `DPS/infDPS/prest/regTrib`, `.../toma/end/endNac`, `.../serv/locPrest/cLocPrestacao`, `.../serv/cServ/cTribNac`, `.../serv/cServ/xDescServ`, `.../valores/vServPrest/vServ`, `.../trib/tribMun`, `.../trib/totTrib`, `infNFSe/valores/vLiq`); escolhas satisfeitas por CNPJ/endNac/cLocPrestacao/CEP | — |
| nfse.xml | 3 | LC116 art. 3 | PASSA | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308` (Aracaju/SE); item 17.19 não figura entre as exceções dos incisos I–XXV do art. 3 → devido no estabelecimento prestador | O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador |
| nfse.xml | 4 | LC123 art. 13 | PASSA | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optante), coerente com perfil "Simples optante"; `regApTribSN = 1`; `tribMun/tribISSQN = 1`; `tpRetISSQN = 1` — sem divergência entre nota e perfil | implica o recolhimento mensal, mediante documento único de arrecadação |
| nfse.xml | 5-aritmética | LC116 art. 7 | PASSA | — | `vLiq` = `vServ` − deduções − retenções = 400,00 − 0,00 (`vCalcDR`) − 0,00 (`vTotalRet` ausente) = 400,00 (confere); sem campo `pAliqAplic` na nota → alíquota implícita `vISSQN/vBC` = 12,00/400,00 = 3,00% (informativa) | A base de cálculo do imposto é o preço do serviço. |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NÃO SE APLICA | — | Prestador optante pelo Simples, atividade contábil (perfil "anexo fixo"): a tabela municipal de alíquotas (IBGE 2800308) não é a alíquota aplicável — o ISS é em valor fixo na forma da lei municipal | constante do inciso XIV do § 5º-B deste artigo recolherá o ISS em valor |
| nfse.xml | 6 | LC214 art. 62 | NÃO SE APLICA | — | A nota não traz o grupo `IBSCBS` (`CST`/`cClassTrib`); nenhum município da carteira expõe IBS/CBS nesta versão | autorizar seus contribuintes a emitir a Nota Fiscal de Serviços Eletrônica de padrão nacional (NFS-e) no ambiente nacional |

Não lidos: nenhum (o arquivo `nfse.xml` é NFS-e do padrão nacional — raiz `NFSe`, `DPS` embutida — e foi auditado).

### The same report in English (verbatim). Not a new audit: the second message of the same conversation asked for the report above in English; the English quotes were looked up in `reference/en/`.

The operator has switched to English. Per the report rules, the quoted excerpts must be verbatim from `reference/en/excerpts/`. Let me pull the English texts.Totals for your comparison: competence 08/2026 = R$ 400.00 (sum of `vServ`; 1 note read)

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | PASS | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (ANEXO B: item 17, subitem 19 → 17.19); profile `item LC 116 = 17.19` — they match | 17.19 – Accounting, including technical and auxiliary services. |
| nfse.xml | 1-descrição | LC116 art. 1 | CANNOT DETERMINE | — | `xDescServ` = "1 Investimento Contábil. 400,00 … Trib aprox…" × description of code 171901 = "Contabilidade, inclusive serviços técnicos e auxiliares." — a judgement about words, not mechanical | The levy of the tax does not depend on the name given to the service rendered. |
| nfse.xml | 2 | `reference/tables/required-fields.md` (all required fields of the path used) | PASS | — | Every `required` element on the branch actually used is present and non-empty (`emit/enderNac`, `DPS/infDPS/prest/regTrib`, `.../toma/end/endNac`, `.../serv/locPrest/cLocPrestacao`, `.../serv/cServ/cTribNac`, `.../serv/cServ/xDescServ`, `.../valores/vServPrest/vServ`, `.../trib/tribMun`, `.../trib/totTrib`, `infNFSe/valores/vLiq`); choices satisfied by CNPJ / endNac / cLocPrestacao / CEP | — |
| nfse.xml | 3 | LC116 art. 3 | PASS | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308` (Aracaju/SE); item 17.19 is not among the exceptions in items I–XXV of art. 3 → due at the provider's establishment | The service is considered rendered, and the tax, due, at the location of the provider's establishment |
| nfse.xml | 4 | LC123 art. 13 | PASS | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optant), coherent with profile "Simples optante"; `regApTribSN = 1`; `tribMun/tribISSQN = 1`; `tpRetISSQN = 1` — no disagreement between note and profile | entails the monthly collection, by means of a single collection document |
| nfse.xml | 5-aritmética | LC116 art. 7 | PASS | — | `vLiq` = `vServ` − deductions − retentions = 400.00 − 0.00 (`vCalcDR`) − 0.00 (`vTotalRet` absent) = 400.00 (checks out); no `pAliqAplic` field on the note → implied rate `vISSQN/vBC` = 12.00/400.00 = 3.00% (informational) | The tax base is the price of the service. |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NOT APPLICABLE | — | Provider is a Simples optant, accounting activity (profile "anexo fixo"): the municipal rate table (IBGE 2800308) is not the applicable rate — the ISS is paid as a fixed amount under municipal law | fixed amount, pursuant to municipal legislation. |
| nfse.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | The note carries no `IBSCBS` group (`CST`/`cClassTrib`); no municipality in the portfolio exposes IBS/CBS in this version | authorize their taxpayers to issue the national-standard Nota Fiscal de Serviços Eletrônica (NFS-e) in the national environment |

Not read: none (the file `nfse.xml` is a national-standard NFS-e — root `NFSe`, embedded `DPS` — and was audited).
