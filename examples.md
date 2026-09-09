# examples.md — worked audits, exactly as the auditor returned them

These are real runs of this folder in a Claude project, on the fixtures in `fixtures/` (anonymised notes of the author's own company, issued by the office), kept **verbatim** — nothing was corrected after the run. Each example says what was fed and in what conditions; the expected result of each run, written before the run, is in `expected/` (outside the loaded set). Each Portuguese report is followed by an English twin. **In examples 1 to 4b the English was produced by the auditor itself**, in the same conversation, on the request "Please repeat the report above in English" — the test being whether it looks the English quotes up in `reference/en/` instead of translating them. It did in examples 1, 3 (on the second answer, after leaving the Portuguese in on the first — kept) and 4b, and the checker confirms every English quote as a verbatim substring of `reference/en/`. **From example 5 on the English is a rendering by the author's session**, not an answer of the auditor: the quotes are looked up in `reference/en/` the same way and checked by the same tool; the Portuguese is the original. Asking the auditor again would have cost the operator a run each time and proved nothing new. What each run showed and what changed in the folder after it, with the commit, is listed in `rounds/fixture-runs-v1/what-changed.md`.

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

## Example 3 — a note with one field altered (m6-valor-liquido: `vLiq` 400.00 → 380.00), with the profile line

**What was fed:** `fixtures/mutations/m6-valor-liquido/nfse.xml` (attached) + the same profile line as example 1.
**Conditions:** same project, `rules.md` at commit 08876fc (check 5 clause added after example 2); model Claude Opus 4.8, effort "low"; 2026-09-09 morning; operator: the author. Expected result, written before the run: `expected/m6-valor-liquido.md` — a FAIL on `5-aritmética`.
**What happened:** the FAIL came, on the right field, with the right arithmetic. Two divergences: (1) severity — the prediction said "bloqueia o fechamento", the auditor said "corrigir antes de fechar", reading `rules.md` § 3 by consequence (a wrong net value does not change the tax); (2) in the English block the auditor kept the Portuguese quotes and explained why, against `rules.md` § 3 and `identity.md`, and offered to swap. Both blocks are kept as they came; what changed after them is in `rounds/fixture-runs-v1/what-changed.md`.

### Report (Portuguese, verbatim)

Now let me verify the service code against ANEXO B and check the excerpts I'll need to cite.The code 171901 is confirmed in ANEXO B (item 17, subitem 19, desdobro 1 — accounting). Now let me verify the place-of-incidence rule for 17.19 and the meaning of the flag values.The place-of-incidence rule is confirmed: **171901 = EP (Estabelecimento do Prestador)** — accounting follows the general rule, not an art. 3 exception. `tpRetISSQN=1` = "Não Retido", `tribISSQN=1` = "Operação tributável". Now let me read the exact excerpts I must quote verbatim.**Totais para a sua comparação:** competência 08/2026 (`dCompet` = 2026-08-31) — **R$ 400,00** (soma de `vServ` das notas lidas).

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | PASSA | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (ANEXO B: item 17 · subitem 19 · desdobro 1); perfil `item LC 116 = 17.19` | "17.19 – Contabilidade, inclusive serviços técnicos e auxiliares." |
| nfse.xml | 1-descrição | LC116 list item 17 | NÃO DÁ PARA DETERMINAR | — | `xDescServ` = "1 Investimento Contábil. 400,00 . Trib aprox R$: 53,80 Federal, R$: 0,00 Estadual e R$: 20,00 Municipal Fonte: IBPT/empresometro.com.br 42CA5A" × descrição do código (`xTribNac`) = "Contabilidade, inclusive serviços técnicos e auxiliares." — a correspondência texto × código é juízo | "17.19 – Contabilidade, inclusive serviços técnicos e auxiliares." |
| nfse.xml | 2 | required-fields.md | PASSA | — | campos obrigatórios do leiaute presentes e não vazios na trilha usada pela nota (`emit/enderNac`; `DPS/infDPS/prest/regTrib` [opSimpNac, regEspTrib]; `toma/end` [endNac, xLgr, nro, xBairro]; `serv/locPrest/cLocPrestacao`; `serv/cServ/cTribNac`; `serv/cServ/xDescServ`; `valores/vServPrest/vServ`; `valores/trib/tribMun`; `valores/trib/totTrib`; `infNFSe/valores/vLiq`) | — |
| nfse.xml | 3 | LC116 art. 3 | PASSA | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`. Item 171901 = LI no Estabelecimento do Prestador (EP) na aba MUN.INCID; não consta das exceções do art. 3º (I–XXV). Tomador em 3505708 é irrelevante para a LI deste item. | "O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador" |
| nfse.xml | 4 | LC123 art. 13 | PASSA | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optante) coerente com perfil "Simples optante"; `regApTribSN = 1`; `regEspTrib = 0`; `valores/trib/tribMun/tribISSQN = 1` (Operação tributável); `tpRetISSQN = 1` (Não Retido) | "recolhimento mensal, mediante documento único de arrecadação" |
| nfse.xml | 5-aritmética | LC116 art. 7 | FALHA | corrigir antes de fechar | `vServ = 400,00`; `vCalcDR = 0,00`; sem desconto/dedução/retenção declarados (`tpRetISSQN = 1` = Não Retido) → `vLiq` esperado = 400,00; `vLiq` declarado = **380,00** (diferença de 20,00, igual a `vTotTribMun = 20,00` — tributo aproximado IBPT, que não é dedução). `vBC = 400,00` está correto. | "A base de cálculo do imposto é o preço do serviço." |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NÃO SE APLICA | — | nota sem campo de alíquota estruturado (`pAliqAplic` ausente); alíquota implícita `vISSQN/vBC` = 8,00/400,00 = 2,00% (informativo). Para optante do Simples (contador em valor fixo) a tabela municipal de alíquotas não é a referência. | "na forma da legislação municipal" |
| nfse.xml | 6 | LC214 art. 62 | NÃO SE APLICA | — | nota sem grupo `IBSCBS` e sem `CST`/`cClassTrib`. Destaque de IBS/CBS torna-se obrigatório nos DFe a partir de 01/01/2026 (notas técnicas) e para optantes do Simples no portal nacional a partir de 01/11/2026; municípios compartilham ao ambiente nacional a partir de 01/01/2026. | "autorizar seus contribuintes a emitir a Nota Fiscal de Serviços Eletrônica de padrão nacional (NFS-e) no ambiente nacional" |

**Não lidos:** nenhum — `nfse.xml` é NFS-e do padrão nacional (raiz `NFSe`, versão 1.01, com `DPS` embutida).

### The same report in English — first answer, kept as it came (the auditor left the Portuguese quotes in, against `rules.md` § 3; the checker reports its rows without gating on them)

<!-- kept-as-came:start -->
**Totals for your comparison:** competence 08/2026 (`dCompet` = 2026-08-31) — **R$ 400.00** (sum of `vServ` of the notes read).

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | PASS | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (ANEXO B: item 17 · subitem 19 · desdobro 1); profile `item LC 116 = 17.19` | "17.19 – Accounting, including technical and auxiliary services." |
| nfse.xml | 1-descrição | LC116 list item 17 | CANNOT DETERMINE | — | `xDescServ` = "1 Investimento Contábil. 400,00 . Trib aprox R$: 53,80 Federal, R$: 0,00 Estadual e R$: 20,00 Municipal Fonte: IBPT/empresometro.com.br 42CA5A" × the code's description (`xTribNac`) = "Contabilidade, inclusive serviços técnicos e auxiliares." — whether the free text matches the code is a judgement | "17.19 – Accounting, including technical and auxiliary services." |
| nfse.xml | 2 | required-fields.md | PASS | — | mandatory layout fields present and non-empty on the path this note uses (`emit/enderNac`; `DPS/infDPS/prest/regTrib` [opSimpNac, regEspTrib]; `toma/end` [endNac, xLgr, nro, xBairro]; `serv/locPrest/cLocPrestacao`; `serv/cServ/cTribNac`; `serv/cServ/xDescServ`; `valores/vServPrest/vServ`; `valores/trib/tribMun`; `valores/trib/totTrib`; `infNFSe/valores/vLiq`) | — |
| nfse.xml | 3 | LC116 art. 3 | PASS | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`. Item 171901 = LI at the Provider's Establishment (EP) in the MUN.INCID sheet; not among the art. 3 exceptions (I–XXV). Taker in 3505708 is irrelevant to the LI of this item. | "O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador" |
| nfse.xml | 4 | LC123 art. 13 | PASS | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optant) coherent with profile "Simples optante"; `regApTribSN = 1`; `regEspTrib = 0`; `valores/trib/tribMun/tribISSQN = 1` (taxable operation); `tpRetISSQN = 1` (not withheld) | "recolhimento mensal, mediante documento único de arrecadação" |
| nfse.xml | 5-aritmética | LC116 art. 7 | FAIL | correct before closing | `vServ = 400.00`; `vCalcDR = 0.00`; no discount/deduction/withholding declared (`tpRetISSQN = 1` = not withheld) → expected `vLiq` = 400.00; declared `vLiq` = **380.00** (difference of 20.00, equal to `vTotTribMun = 20.00` — IBPT approximate tax, which is not a deduction). `vBC = 400.00` is correct. | "A base de cálculo do imposto é o preço do serviço." |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NOT APPLICABLE | — | note carries no structured rate field (`pAliqAplic` absent); implied rate `vISSQN/vBC` = 8.00/400.00 = 2.00% (informational). For a Simples optant (accountant at a fixed amount) the municipal rate table is not the reference. | "na forma da legislação municipal" |
| nfse.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | note has no `IBSCBS` group and no `CST`/`cClassTrib`. IBS/CBS highlighting becomes mandatory on electronic fiscal documents from 01/01/2026 (technical notes) and for Simples optants on the national portal from 01/11/2026; municipalities share to the national environment from 01/01/2026. | "autorizar seus contribuintes a emitir a Nota Fiscal de Serviços Eletrônica de padrão nacional (NFS-e) no ambiente nacional" |

**Not read:** none — `nfse.xml` is a national-standard NFS-e (root `NFSe`, version 1.01, with the embedded `DPS`).

Note on the excerpts: the quoted provisions stay in Portuguese here because the standard is the Portuguese text and the English texts in `reference/en/` are machine translations kept only so a citation can be followed — the header note in `INDEX.md` is explicit that the Portuguese is the standard. The item-17 line is shown in English above because it is a lookup label from ANEXO B, not a cited provision. If you want the English `reference/en/` wording placed in the "quoted excerpt" column instead, say so and I'll swap them.
<!-- kept-as-came:end -->

### The same report in English — second answer, after the operator pointed at `rules.md` § 3 ("Yes, swap them: rules.md § 3 says the quoted excerpt in an English report is the reference/en/ text of the same provision"), verbatim. Not a new audit.

Right — per rules.md § 3 the quoted excerpt in an English report comes from `reference/en/`. Swapped in below.

**Totals for your comparison:** competence 08/2026 (`dCompet` = 2026-08-31) — **R$ 400.00** (sum of `vServ` of the notes read).

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | PASS | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (ANEXO B: item 17 · subitem 19 · desdobro 1); profile `item LC 116 = 17.19` | "17.19 – Accounting, including technical and auxiliary services." |
| nfse.xml | 1-descrição | LC116 list item 17 | CANNOT DETERMINE | — | `xDescServ` = "1 Investimento Contábil. 400,00 . Trib aprox R$: 53,80 Federal, R$: 0,00 Estadual e R$: 20,00 Municipal Fonte: IBPT/empresometro.com.br 42CA5A" × the code's description (`xTribNac`) = "Contabilidade, inclusive serviços técnicos e auxiliares." — whether the free text matches the code is a judgement | "17.19 – Accounting, including technical and auxiliary services." |
| nfse.xml | 2 | required-fields.md | PASS | — | mandatory layout fields present and non-empty on the path this note uses (`emit/enderNac`; `DPS/infDPS/prest/regTrib` [opSimpNac, regEspTrib]; `toma/end` [endNac, xLgr, nro, xBairro]; `serv/locPrest/cLocPrestacao`; `serv/cServ/cTribNac`; `serv/cServ/xDescServ`; `valores/vServPrest/vServ`; `valores/trib/tribMun`; `valores/trib/totTrib`; `infNFSe/valores/vLiq`) | — |
| nfse.xml | 3 | LC116 art. 3 | PASS | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`. Item 171901 = LI at the Provider's Establishment (EP) in the MUN.INCID sheet; not among the art. 3 exceptions (I–XXV). Taker in 3505708 is irrelevant to the LI of this item. | "The service is considered rendered, and the tax, due, at the location of the provider's establishment" |
| nfse.xml | 4 | LC123 art. 13 | PASS | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optant) coherent with profile "Simples optante"; `regApTribSN = 1`; `regEspTrib = 0`; `valores/trib/tribMun/tribISSQN = 1` (taxable operation); `tpRetISSQN = 1` (not withheld) | "the monthly collection, by means of a single collection document" |
| nfse.xml | 5-aritmética | LC116 art. 7 | FAIL | correct before closing | `vServ = 400.00`; `vCalcDR = 0.00`; no discount/deduction/withholding declared (`tpRetISSQN = 1` = not withheld) → expected `vLiq` = 400.00; declared `vLiq` = **380.00** (difference of 20.00, equal to `vTotTribMun = 20.00` — IBPT approximate tax, which is not a deduction). `vBC = 400.00` is correct. | "The tax base is the price of the service." |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NOT APPLICABLE | — | note carries no structured rate field (`pAliqAplic` absent); implied rate `vISSQN/vBC` = 8.00/400.00 = 2.00% (informational). For a Simples optant (accountant at a fixed amount) the municipal rate table is not the reference. | "pursuant to municipal legislation" |
| nfse.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | note has no `IBSCBS` group and no `CST`/`cClassTrib`. IBS/CBS highlighting becomes mandatory on electronic fiscal documents from 01/01/2026 (technical notes) and for Simples optants on the national portal from 01/11/2026; municipalities share to the national environment from 01/01/2026. | "authorize their taxpayers to issue the national-standard Nota Fiscal de Serviços Eletrônica (NFS-e) in the national environment" |

**Not read:** none — `nfse.xml` is a national-standard NFS-e (root `NFSe`, version 1.01, with the embedded `DPS`).

The `xTribNac` value shown in the 1-descrição location stays in Portuguese because it is the note's own field content, not a cited provision.

## Example 4 — a correct note (nfse-02) fed WITHOUT the profile line: the null case

**What was fed:** `fixtures/clean/nfse-02.xml` (attached), and nothing else — no profile line, no text in the message.
**Conditions:** same project, `rules.md` at commit 78965ed; model Claude Opus 4.8, effort "low"; 2026-09-09 ~10:45; operator: the author. Expected result, written 09/09 08:42 before the run: `expected/nfse-02-sem-perfil.md` — CANNOT DETERMINE on `1-código`, `1-descrição`, `4` and `5-alíquota`; PASS on `2`, `3`, `5-aritmética`; NOT APPLICABLE on `6`.
**What happened — three divergences, all of one kind: the auditor supplied what the profile line did not.** (1) With no text in the message it decided "the operator is writing in English" and answered in English (`rules.md` § 3: Portuguese by default). (2) `1-código` came back PASS because the code exists in ANEXO B, with "match to the client's item not verified" written in the location column — the rule says no profile line → CANNOT DETERMINE; a code that exists is not a code that is right for this client. (3) `5-alíquota` came back NOT APPLICABLE by reading the note's own flag (`opSimpNac = 3`) and its free text ("Fixo Contador") as the client's regime — the rule says the regime comes from the profile line, never inferred from the note. `4` did come back CANNOT DETERMINE, correctly. The answer is kept as it came; the second message ("in English") returned the same report and is not repeated here. What changed after this run is in `rounds/fixture-runs-v1/what-changed.md`; the re-run with the corrected `rules.md` is example 4b below.

### Report (verbatim — came in English although no text was sent)

I'll read the framework files first, then process the XML. Let me start with the core rules and identity.Now the uploaded note:A valid national-standard note. No profile line was pasted, so profile-dependent checks return CANNOT DETERMINE. The operator is writing in English, so the report and quoted excerpts will be in English. Let me pull the English excerpts and do the required lookups.Let me verify the code exists in ANEXO B, confirm the municipality codes, and check the remaining required-field lines for check 2.**Totals for your comparison:** R$ 400,00 — competence 2026-09 (`dCompet` 2026-09-05), from 1 note read.

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse-02.xml (nNFSe 5) | 1-código | LC116 list item 17 | PASS | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` — exists in ANEXO B (item 17 / subitem 19 / desdobro 01). Match to the client's registered LC 116 item not verified (no profile line). | 17.19 – Accounting, including technical and auxiliary services. |
| nfse-02.xml (nNFSe 5) | 1-descrição | LC116 art. 1 | CANNOT DETERMINE | — | `serv/cServ/xDescServ` = "1 Investimento Contábil. 400,00 …" vs `cTribNac`/`xTribNac` = "Contabilidade, inclusive serviços técnicos e auxiliares." (171901) — whether the free text matches the code is a judgement. | The levy of the tax does not depend on the name given to the service rendered. |
| nfse-02.xml (nNFSe 5) | 2 | required-fields.md (ANEXO I / XSD v1.01) | PASS | — | All elements marked *required* on the path this note uses are present and non-empty (provider-issued domestic note, `tpEmit=1`; no `comExt`/`obra`/`atvEvento`/`IBSCBS` groups). | — |
| nfse-02.xml (nNFSe 5) | 3 | LC116 art. 3 | PASS | — | `infNFSe/cLocIncid = 2800308` (Aracaju/SE) = `DPS/infDPS/cLocEmi = 2800308`. Item 17.19 is not among the art. 3 exceptions (I–XXV); default rule (provider establishment) applies. Taker in `toma/end/endNac/cMun = 3505708` (Barueri/SP) does not shift incidence. | The service is considered rendered, and the tax due, at the location of the provider's establishment |
| nfse-02.xml (nNFSe 5) | 4 | LC123 art. 13 | CANNOT DETERMINE | — | `prest/regTrib/opSimpNac = 3` (optant); `regApTribSN = 1`; `regEspTrib = 0`; `valores/trib/tribMun/tribISSQN = 1`; `tpRetISSQN = 1`. No profile line to confirm these match the client's registered regime — verify the client's registration, do not infer it from the note. | Simples Nacional entails the monthly collection, by means of a single collection document, of the following taxes and contributions |
| nfse-02.xml (nNFSe 5) | 5-aritmética | LC116 art. 7 | PASS | — | `vLiq = 400.00` = `vServ 400.00` − deductions `0.00` (`vCalcDR 0.00`) − retentions `0.00` (no `vTotalRet`). | The tax base is the price of the service. |
| nfse-02.xml (nNFSe 5) | 5-alíquota | LC123 art. 18 §22-A | NOT APPLICABLE | — | No `pAliqAplic` field on the note. Implied rate `vISSQN 8.00 / vBC 400.00 = 2%` (informational). Optant declared (`opSimpNac=3`), accounting-fixed (`xOutInf`: "Optante do Simples Nacional Fixo Contador"): the Aracaju municipal rate table does not apply. | The activity set forth in item XIV of § 5-B of this article shall pay ISS in a fixed amount, pursuant to municipal legislation. |
| nfse-02.xml (nNFSe 5) | 6 | LC214 art. 62 | NOT APPLICABLE | — | No `CST`/`cClassTrib`/`IBSCBS` group on the note. IBS/CBS exposure on electronic fiscal documents phases in from 01/01/2026 (national portal for Simples optants from 01/11/2026); no portfolio municipality exposes the fields yet. | authorize their taxpayers to issue the national-standard Nota Fiscal de Serviços Eletrônica (NFS-e) in the national environment |

**Not read:** none — the file is a national-standard NFS-e (root `NFSe`, versão 1.01, embedded `DPS`).

## Example 4b — the null case again, after the correction (nfse-02 without the profile line)

**What was fed:** `fixtures/clean/nfse-02.xml` (attached), and nothing else — no text in the message. A new conversation.
**Conditions:** same project with `rules.md` at commit f38ec00 (the three clauses added after example 4); model Claude Opus 4.8, effort "low"; 2026-09-09 ~11:15; operator: the author. Expected result: `expected/nfse-02-sem-perfil.md` (unchanged since 08:42).
**What happened:** the report matches the prediction row by row — Portuguese with no text in the message; CANNOT DETERMINE on `1-código` ("a code that exists is not a code that is right for this client"), `1-descrição`, `4` and `5-alíquota`; PASS on `2`, `3`, `5-aritmética`; NOT APPLICABLE on `6`. Check 4 cites LC123 art. 18 §5º-B (item XIV, accounting offices) instead of art. 13 — both are in the check's list.

### Report (Portuguese, verbatim)

Totais para a sua comparação: 09/2026 — R$ 400,00.

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-02.xml | 1-código | LC116 list item 17 | NÃO DÁ PARA DETERMINAR | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (existe no ANEXO B: item 17, subitem 19, desdobro 1). Falta a linha de perfil: um código que existe não é um código certo para este cliente. | "Contabilidade, inclusive serviços técnicos e auxiliares." |
| nfse-02.xml | 1-descrição | LC116 list item 17 | NÃO DÁ PARA DETERMINAR | — | `xDescServ = "1 Investimento Contábil. 400,00 ..."` × descrição do código `171901 = "Contabilidade, inclusive serviços técnicos e auxiliares."` — juízo sobre palavras. | "Contabilidade, inclusive serviços técnicos e auxiliares." |
| nfse-02.xml | 2 | ANEXO I / XSD v1.01 (required-fields.md) | PASSA | — | Todos os campos obrigatórios presentes e não vazios no caminho usado pela nota (`emit`, `emit/enderNac`, `prest/regTrib` [`opSimpNac`, `regEspTrib`], `toma` [`xNome`, `end/xLgr`, `nro`, `xBairro`], `serv/cServ` [`cTribNac`, `xDescServ`], `valores/vServPrest/vServ`, `trib/tribMun`, `trib/totTrib`, `infNFSe/valores/vLiq`). | — |
| nfse-02.xml | 3 | LC116 art. 3 | PASSA | — | Item 17.19 não consta das exceções dos incisos I–XXV (do item 17, só 17.05 e 17.10). Regra padrão: devido no estabelecimento prestador. `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308` (Aracaju). | "O serviço considera-se prestado e o imposto devido no local do estabelecimento prestador" |
| nfse-02.xml | 4 | LC123 art. 18 §5º-B | NÃO DÁ PARA DETERMINAR | — | `prest/regTrib/opSimpNac = 3`, `regApTribSN = 1`, `tribMun/tribISSQN = 1`, `tpRetISSQN = 1` são coerentes entre si; falta a linha de perfil para confrontar com o `regime` cadastral do cliente. As flags da própria nota não substituem o perfil. | "XIV - escritórios de serviços contábeis, observado o disposto nos §§ 22-B e 22-C deste artigo." |
| nfse-02.xml | 5-aritmética | LC116 art. 7 | PASSA | — | `vLiq = 400,00` = `vServ = 400,00` − 0 (sem descontos) − 0 (sem retenção; `tpRetISSQN = 1` = não retido). Fecha. | "A base de cálculo do imposto é o preço do serviço." |
| nfse-02.xml | 5-alíquota | LC123 art. 18 §22-A | NÃO DÁ PARA DETERMINAR | — | Sem campo de alíquota (`pAliqAplic` ausente): alíquota implícita `vISSQN/vBC = 8,00/400,00 = 2,0%` fica apenas informativa. Sem a linha de perfil não se confirma o regime que fixa a alíquota aplicável (optante → ISS no DAS / valor fixo do contador). | "recolherá o ISS em valor fixo, na forma da legislação municipal." |
| nfse-02.xml | 6 | LC214 art. 62 | NÃO SE APLICA | — | Nenhum município da carteira expõe ainda os campos IBS/CBS; a nota não carrega `CST`/`cClassTrib` (grupo `IBSCBS` ausente). Reentra quando uma nota real trouxer esses campos. | "os Municípios e o Distrito Federal ficam obrigados, a partir de 1º de janeiro de 2026" |

Não lidos: nenhum.

### The same report in English (verbatim; second message of the same conversation; not a new audit)

Totals for your comparison: 09/2026 — R$ 400.00

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse-02.xml | 1-código | LC116 list item 17 | CANNOT DETERMINE | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (exists in ANEXO B: item 17, subitem 19, breakdown 1). No profile line: a code that exists is not a code that is right for this client. | "Accounting, including technical and auxiliary services." |
| nfse-02.xml | 1-descrição | LC116 list item 17 | CANNOT DETERMINE | — | `xDescServ = "1 Investimento Contábil. 400,00 ..."` × description of code `171901 = "Contabilidade, inclusive serviços técnicos e auxiliares."` — a judgement about words. | "Accounting, including technical and auxiliary services." |
| nfse-02.xml | 2 | ANEXO I / XSD v1.01 (required-fields.md) | PASS | — | Every required element is present and non-empty on the path the note uses (`emit`, `emit/enderNac`, `prest/regTrib` [`opSimpNac`, `regEspTrib`], `toma` [`xNome`, `end/xLgr`, `nro`, `xBairro`], `serv/cServ` [`cTribNac`, `xDescServ`], `valores/vServPrest/vServ`, `trib/tribMun`, `trib/totTrib`, `infNFSe/valores/vLiq`). | — |
| nfse-02.xml | 3 | LC116 art. 3 | PASS | — | Item 17.19 is not among the exceptions of items I–XXV (of item 17, only 17.05 and 17.10). Default rule: due at the provider's establishment. `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308` (Aracaju). | "The service is considered rendered, and the tax due, at the location of the provider's establishment" |
| nfse-02.xml | 4 | LC123 art. 18 §5º-B | CANNOT DETERMINE | — | `prest/regTrib/opSimpNac = 3`, `regApTribSN = 1`, `tribMun/tribISSQN = 1`, `tpRetISSQN = 1` are coherent among themselves; the profile line is missing to confront them with the client's registered `regime`. The note's own flags do not replace the profile. | "offices, observing the provisions of §§ 22-B and 22-C of this article." |
| nfse-02.xml | 5-aritmética | LC116 art. 7 | PASS | — | `vLiq = 400.00` = `vServ = 400.00` − 0 (no discounts) − 0 (no retention; `tpRetISSQN = 1` = not retained). Adds up. | "The tax base is the price of the service." |
| nfse-02.xml | 5-alíquota | LC123 art. 18 §22-A | CANNOT DETERMINE | — | No rate field (`pAliqAplic` absent): the implied rate `vISSQN/vBC = 8.00/400.00 = 2.0%` is informational only. Without the profile line the regime that fixes the applicable rate cannot be confirmed (optant → ISS inside the DAS / accountant's fixed amount). | "fixed amount, pursuant to municipal legislation." |
| nfse-02.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | No municipality in the office's portfolio exposes the IBS/CBS fields yet; the note carries no `CST`/`cClassTrib` (the `IBSCBS` group is absent). Re-enters when a real note carries those fields. | "the Municipalities and the Federal District are required, as of January 1, 2026" |

Not read: none.
