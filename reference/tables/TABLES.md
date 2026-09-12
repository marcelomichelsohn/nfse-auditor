# tables/ — lookups beside the standard (not the standard)

Two kinds of file live here, and the difference matters to a reader checking a report.

## Official tables (`official/`)
Downloaded on 07/09/2026 from the national NFS-e documentation page — https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual — file names as published; hashes in `official/SHA256SUMS.txt`.
- **ANEXO_B** (`oficial_anexo_b-…xlsx`): the national service list — the `cTribNac` codes (LC 116 item / sub-item / breakdown) and the NBS 2.0 list. Check 1 verifies that a note's `cTribNac` exists here; the rule cited is LC 116.
- **ANEXO_C** (`oficial_anexo-c-…xlsx`): `indOp` codes (place of the operation for IBS/CBS, LC 214 art. 11) and `cClassTrib`. Not used by v1 checks (IBS/CBS = NOT APPLICABLE).
- **ANEXO_A** (`oficial_anexo_a-…xlsx`): IBGE municipality codes and ISO2 country codes. Check 3 resolves `cLocEmi`, `cLocPrestacao`, `cLocIncid`; a foreign taker's country.
- **ANEXO_I** (`oficial_anexo_i-…xlsx`) and the **XSD v1.01** zip: the DPS/NFS-e layout. `required-fields.md` is generated from the XSD (script, 08/09/2026) and is what check 2 reads.
- `tabela-indoper.xlsx`: the indOper table as delivered by the office (39 codes); its codes match ANEXO_C; origin not stated in the file.

### `official/csv/` and `official/xsd/` — the same official files in a form a project can load
A Claude project refuses `.zip` and reads `.xlsx` poorly (found on 09/09/2026, first load). So: every sheet of every official `.xlsx` above is exported to `official/csv/<file>__<sheet>.csv` by `tools/xlsx_to_csv.py` (values as they are, empty rows dropped, one file per sheet; hashes and date in `official/csv/SHA256SUMS.txt`), and the ten `.xsd` of the layout are unpacked from the zip into `official/xsd/`. **The `.xlsx` and the `.zip` remain the official files**; the CSV and the unpacked XSD are the author's conversion of them, and a reader who doubts a CSV opens the `.xlsx` beside it. The project loads the CSV; it does not need the XSD (`required-fields.md` is what check 2 reads).

## Municipal ISS rates — one municipality only
`municipal-rates_2800308-aracaju-se_extract-20260903.csv`: the rows of IBGE code 2800308 (Aracaju/SE) cut from the official extraction `aliquotas-municipios-20260903-extr1.zip` published 03/09/2026 on https://www.gov.br/nfse/pt-br/biblioteca/perguntas-e-respostas/aliquotas (columns as published: `codigo_ibge;uf;nome_municipio;codigo_servico;incidencia;aliquota;dt_ini;dt_fim`). The whole file (5,571 municipalities, 277 MB) is not here. **This table is not the rate applicable to a Simples Nacional optant:** for an optant the ISS is paid inside the DAS (LC 123 art. 13 VIII), and for an accounting society it is a fixed amount (DL 406 art. 9 §§1, 3; LC 123 art. 18 §22-A). It is kept so that a NOT APPLICABLE row on the rate can be checked against the table it does not apply.

## The office's working tables (`working/`) — why they are here and what they are not
The office that uses this auditor sent two conversion tables it works with. **They are not official documents**: no government site publishes these joins. They are compilations built from official sources, by the office or by its software vendor. They are shipped here so that a reader does not have to open the Portuguese official sites to follow a lookup — and each column below says which official file it comes from, with the link. A report row never cites these tables as a rule; it cites LC 116 or the official annex.

### `01_cnae_para_lc116.csv` — CNAE sub-class → LC 116 item (2,353 rows)
| Column | Meaning (EN) | Official source of the values |
|---|---|---|
| `cnae_subclasse`, `cnae_mascara`, `cnae_descricao` | CNAE 2.3 sub-class code, formatted code, description | IBGE / CONCLA — https://concla.ibge.gov.br/busca-online-cnae.html |
| `item_lc116`, `descricao_atividade_lc` | LC 116 service item and its wording | LC 116/2003 annexed list — `../pt/full/lc116-2003_iss.txt`; https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm |
| *(the join CNAE → item)* | which item a CNAE usually maps to | **the office's working rule** — no official publication; use as a hint, confirm on the note's description and the client's registration |

### `02_lc116_para_nbs_cclasstrib.csv` — LC 116 item → NBS → indOp → cClassTrib (1,739 rows)
| Column | Meaning (EN) | Official source of the values |
|---|---|---|
| `item_lc116`, `descricao_item` | LC 116 item and wording | LC 116/2003 list (as above) |
| `nbs`, `descricao_nbs` | NBS 2.0 code and description | NBS 2.0 Anexo I — `../pt/full/nbs-v2.0_anexo-i.txt`; https://www.gov.br/mdic/pt-br/assuntos/sdic/comercio-e-servicos/nbs-nomenclatura-brasileira-de-servicos; ANEXO_B (`official/`) |
| `ps_onerosa`, `adq_exterior` | service for consideration; acquirer abroad (flags) | office's working flags |
| `indop`, `local_incidencia_ibs` | place-of-operation code and its description (IBS/CBS) | ANEXO_C (`official/`); LC 214 art. 11 |
| `cclasstrib`, `nome_cclasstrib` | tax classification code and name (IBS/CBS) | IT 2025.002 v1.40 — `../pt/full/it-2025-002-v1.40_tabelas-cst-cclasstrib.txt` |
| *(the joins)* | item ↔ NBS ↔ indOp ↔ cClassTrib | **the office's working rule** — no official publication |

**Known mismatches, re-counted on 11/09/2026:** the second table uses 674 distinct NBS codes, and **all 674 are in the official NBS list** (ANEXO_B, `official/csv/…LISTA_NBS_v2_0.csv`). This line said 675 codes of which 582 existed, counted on 07/09; both halves were wrong, and the truth is the better news. Re-derive with the `nbs` column of `working/02_lc116_para_nbs_cclasstrib.csv` against that file, comparing with the dots stripped; its `indop` column has 24 distinct values, 11 of them written exactly as in ANEXO_C (the others look like the same codes with leading zeros dropped). Nothing was corrected: the tables are shipped as received, hashed in `working/SHA256SUMS.txt`.
