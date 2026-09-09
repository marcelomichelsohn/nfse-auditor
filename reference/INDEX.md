# reference/INDEX.md — everything the auditor may cite, and where to check it

**Rule.** A report row cites one of the provision ids below (column *Cite as*). The quoted excerpt must be a verbatim substring of the Portuguese text in `pt/` (or of the English text in `en/` for a report written in English); `tools/check_audit.py` checks it. Tables are lookups, never provisions: a row may say "code not in ANEXO_B", but the rule it cites is LC 116.

## Texts (official, as delivered; PT original + EN machine translation beside)

| Id | Document | PT full | EN full | Official source | Captured | SHA256 (PT text, first 16 hex) |
|---|---|---|---|---|---|---|
| LC116 | Lei Complementar 116/2003 — ISS | `pt/full/lc116-2003_iss.txt` (text) · `pt/full/lc116-2003_iss.pdf` (original) | `en/full/lc116-2003_iss.en.txt` | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm | 07/09/2026 | `71ba8383b7092d0a…` |
| LC123 | Lei Complementar 123/2006 — Simples Nacional | `pt/full/lc123-2006_simples-nacional.txt` (text) · `pt/full/lc123-2006_simples-nacional.html` (original) | `en/full/lc123-2006_simples-nacional.en.txt` | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm | 07/09/2026 | `c35093f3aac948c1…` |
| DL406 | Decreto-Lei 406/1968 — ISS (fixed-amount ISS, art. 9) | `pt/full/dl406-1968_iss-fixo.txt` (text) · `pt/full/dl406-1968_iss-fixo.html` (original) | `en/full/dl406-1968_iss-fixo.en.txt` | https://www.planalto.gov.br/ccivil_03/decreto-lei/del0406.htm | 07/09/2026 | `b028a0aed31ac4e2…` |
| LC214 | Lei Complementar 214/2025 — IBS, CBS, IS | `pt/full/lc214-2025_ibs-cbs.txt` (text) · `pt/full/lc214-2025_ibs-cbs.pdf` (original) | `en/full/lc214-2025_ibs-cbs.en.txt` | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | 07/09/2026 | `1b83b4af730c2d05…` |
| RFB2026 | Receita Federal — Orientações 2026 (Reforma Tributária do Consumo) | `pt/full/rfb-orientacoes-2026_reforma-tributaria.txt` (text) · `pt/full/rfb-orientacoes-2026_reforma-tributaria.html` (original) | `en/full/rfb-orientacoes-2026_reforma-tributaria.en.txt` | https://www.gov.br/receitafederal/pt-br/assuntos/reforma-tributaria-do-consumo/orientacoes-2026 | 07/09/2026 | `7ef8cfcce9ed7570…` |
| IT2025002 | Informe Técnico 2025.002 v1.40 — cClassTrib / CST tables (IBS/CBS) | `pt/full/it-2025-002-v1.40_tabelas-cst-cclasstrib.txt` (text) · `pt/full/it-2025-002-v1.40_tabelas-cst-cclasstrib.pdf` (original) | `en/full/it-2025-002-v1.40_tabelas-cst-cclasstrib.en.txt` | NF-e project (Reforma Tributária do Consumo), document dated 27/01/2026 — delivered by the office; official portal: https://www.nfe.fazenda.gov.br | 07/09/2026 | `d5bbdcb83f63c196…` |
| NBS | Nomenclatura Brasileira de Serviços 2.0 — Anexo I | `pt/full/nbs-v2.0_anexo-i.txt` (text) · `pt/full/nbs-v2.0_anexo-i.pdf` (original) | `en/full/nbs-v2.0_anexo-i.en.txt` | https://www.gov.br/mdic/pt-br/assuntos/sdic/comercio-e-servicos/nbs-nomenclatura-brasileira-de-servicos | 07/09/2026 | `0092383d92dd04f8…` |

The English texts are machine translations by parallel agents, accepted as they came (LC 116, LC 214, IT 2025.002, NBS on 07/09/2026; LC 123, DL 406, RFB 2026 on 08/09/2026), checked for completeness by counts of articles, paragraphs, items and sub-items against the Portuguese. They exist so that a reader who does not read Portuguese can follow a citation; **the Portuguese text is the standard.** Full hashes: `pt/full/SHA256SUMS.txt`, `en/full/SHA256SUMS.txt`.

## Provisions the auditor cites (excerpts — each a verbatim substring of its full text, checked by C0)

| Cite as | Excerpt PT | Excerpt EN | What it governs |
|---|---|---|---|
| **LC116 art. 1** | `pt/excerpts/lc116_art1-2.txt` | `en/excerpts/lc116_art1-2.en.txt` | incidence of ISS; service list annexed |
| **LC116 art. 2** | `pt/excerpts/lc116_art1-2.txt` | `en/excerpts/lc116_art1-2.en.txt` | non-incidence — I: export of services |
| **LC116 art. 3** | `pt/excerpts/lc116_art3.txt` | `en/excerpts/lc116_art3.en.txt` | place where the service is deemed rendered / tax due (exceptions I–XXV) |
| **LC116 art. 4** | `pt/excerpts/lc116_art4-5.txt` | `en/excerpts/lc116_art4-5.en.txt` | provider establishment |
| **LC116 art. 5** | `pt/excerpts/lc116_art4-5.txt` | `en/excerpts/lc116_art4-5.en.txt` | taxpayer = provider |
| **LC116 art. 7** | `pt/excerpts/lc116_art7.txt` | `en/excerpts/lc116_art7.en.txt` | tax base = price of the service |
| **LC116 art. 8** | `pt/excerpts/lc116_art8-8A.txt` | `en/excerpts/lc116_art8-8A.en.txt` | maximum rates |
| **LC116 art. 8-A** | `pt/excerpts/lc116_art8-8A.txt` | `en/excerpts/lc116_art8-8A.en.txt` | minimum rate 2% |
| **LC116 list item 17** | `pt/excerpts/lc116_lista_item17.txt` | `en/excerpts/lc116_lista_item17.en.txt` | item 17 group (17.01–17.25), incl. 17.19 accounting |
| **LC123 art. 13** | `pt/excerpts/lc123_art13.txt` | `en/excerpts/lc123_art13.en.txt` | Simples = single monthly document; VIII: ISS inside the DAS |
| **LC123 art. 18 §5º-B** | `pt/excerpts/lc123_art18_par5B.txt` | `en/excerpts/lc123_art18_par5B.en.txt` | activities taxed under Anexo III — XIV: accounting services |
| **LC123 art. 18 §22-A** | `pt/excerpts/lc123_art18_par22A.txt` | `en/excerpts/lc123_art18_par22A.en.txt` | accounting activity pays ISS at a fixed amount under municipal law |
| **DL406 art. 9** | `pt/excerpts/dl406_art9.txt` | `en/excerpts/dl406_art9.en.txt` | tax base; §1 fixed-amount ISS for personal work; §3 societies of professionals |
| **LC214 art. 62** | `pt/excerpts/lc214_art62.txt` | `en/excerpts/lc214_art62.en.txt` | municipalities must authorise the national-standard NFS-e / share documents to the national environment from 01/01/2026 |
| **RFB 2026 — Orientações** | `pt/excerpts/rfb2026_orientacoes.txt` | `en/excerpts/rfb2026_orientacoes.en.txt` | CBS/IBS highlight in electronic fiscal documents from 01/01/2026 per the technical notes |
| **IT 2025.002 — header** | `pt/excerpts/it2025002_cabecalho.txt` | `en/excerpts/it2025002_cabecalho.en.txt` | identification of the cClassTrib/CST tables (version, date) |

## Tables (lookups)

| Table | File | Source | Used by |
|---|---|---|---|
| ANEXO_B — national service list × NBS 2.0 (v1.01, 22/01/2026) | `tables/official/oficial_anexo_b-nbs2-lista_servico_nacional-snnfse-v1-01-20260122.xlsx` | https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual | cTribNac codes (item/subitem/desdobro) — check 1 |
| ANEXO_C — indOp / cClassTrib (v1.01) | `tables/official/oficial_anexo-c-indop-ibscbs-snnfse-v1-01.xlsx` | same page | place-of-incidence codes for IBS/CBS (v2 only) |
| ANEXO_A — IBGE municipality codes / ISO2 countries (v1.00, 10/12/2025) | `tables/official/oficial_anexo_a-municipio_ibge-paises_iso2-v1-00-snnfse-20251210.xlsx` | same page | cMun / cLocIncid / cLocPrestacao resolution — check 3; country of a foreign taker |
| ANEXO_I — DPS/NFS-e layout (SEFIN ADN, v1.01, 09/02/2026) | `tables/official/oficial_anexo_i-sefin_adn-dps_nfse-snnfse-v1-01-20260209.xlsx` | same page | field definitions — check 2 |
| XSD schemas v1.01 (09/02/2026) | `tables/official/oficial_nfse-esquemas_xsd-v1-01-20260209.zip` | same page | required elements — extracted to `tables/required-fields.md` — check 2 |
| Required fields (generated from the XSD) | `tables/required-fields.md` | generated 08/09/2026 by script from the zip above | check 2 |
| indOper table (39 codes, valid from 17/11/2025) | `tables/official/tabela-indoper.xlsx` | delivered by the office; matches ANEXO_C codes — origin not stated in the file | v2 only |
| Municipal ISS rates — rows of IBGE 2800308 (Aracaju/SE) only, from the official extraction of 03/09/2026 | `tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` | https://www.gov.br/nfse/pt-br/biblioteca/perguntas-e-respostas/aliquotas (file aliquotas-municipios-20260903-extr1.zip, 03/09/2026 15:33) | check 5 — NOT the applicable rate for a Simples optant (LC123 art. 13 VIII); kept as the excerpt that supports NOT APPLICABLE |
| Office working table — CNAE → LC 116 item | `tables/working/01_cnae_para_lc116.csv` | compiled by the office — see `tables/README.md` | lookup only for check 1; never cited as a provision |
| Office working table — LC 116 item → NBS → indOp → cClassTrib | `tables/working/02_lc116_para_nbs_cclasstrib.csv` | compiled by the office — see `tables/README.md` | lookup only (v2); never cited as a provision |

## Not in this folder, on purpose
- The full municipal rate extraction (277 MB, 5,571 municipalities): only the rows of the municipality of the tested notes are here, with the source and date of the official file.
- Any client document. Fixtures live in `../fixtures/`, anonymised; expected results in `../expected/`.
- Any summary of a law written by the authors: what is cited is the text.
