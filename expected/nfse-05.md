# expected — nfse-05 (a note of a client of the office, national standard, August 2026)

**What was fed:** `fixtures/client/nfse-05.xml` + the profile line `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702`.
The regime cell and the `Código de Atividade` cell are the office's own, as round 2 recorded them (`../rounds/round-2-v2/report-1.md`, rows `1-código` and `4`). The `Anexo` cell is written in the sheet's style: **no check of this version reads it** (`rules.md` § 0).

**Where this note comes from.** A real NFS-e issued by a client of the accounting office, anonymised by `../tools/anonymise.py` and by no other path, under the office's confidentiality agreement of 11/09/2026, whose condition is no client name and no CNPJ in a public repository (`../rounds/CONSENT.md`, point 3). The issuer here is not an accounting office, so its placeholder is `PRESTADOR 02 LTDA`, kept distinct from the `PRESTADOR CONTABIL LTDA` of `fixtures/clean/`: a mask that renamed a security-and-solar company into an accounting firm would make the report read as nonsense.

**This is one of the two notes the office actually audited.** The report the operator received for it, as it came, is `../rounds/round-2-v2/report-2.md`. This file says what a correct audit must return; that one is what a real audit did return, on the office's account, on this note. A reader can run the note and hold the three side by side.

**This file is outside the folder the operator loads.** It says what a correct audit must return, row by row; a row's quote must be a verbatim substring of `reference/pt/`. The CSV block that closes a report repeats these rows with the full location and is not predicted here row by row: same content, other shape.

Totais para a sua comparação: 08/2026 — R$ 290,00 (1 nota lida).

| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-05.xml | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 list item 7 | FALHA | corrigir antes de fechar · você decide antes de fechar | `DPS/infDPS/serv/cServ/cTribNac = 310101` (item 31.01, "Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres.") × perfil `Código de Atividade = 702` (item 7.02, obras de construção civil e instalação e montagem de produtos, peças e equipamentos) | "7.02 – Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou" |
| nfse-05.xml | 1-descrição · descrição escrita pelo cliente comparada com a descrição oficial do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | `xDescServ = "Instalação de Hd de 1tb"` × descrição oficial do código `310101` — coincidência texto × código é juízo | "A incidência do imposto não depende da denominação dada ao serviço prestado." |
| nfse-05.xml | 2 · campos obrigatórios do leiaute nacional | required-fields.md (ANEXO I / XSD v1.01) | PASSA | — | (todos os campos obrigatórios preenchidos) | — |
| nfse-05.xml | 3 · município onde o ISS é devido | LC116 art. 3 | PASSA | — | `infNFSe/cLocIncid = 2800308` = `DPS/infDPS/cLocEmi = 2800308`; item 31.01 não consta das exceções I–XXV (regra geral) | "O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador" |
| nfse-05.xml | 4 · marcações do Simples Nacional comparadas com o regime do cadastro | LC123 art. 13 | PASSA | — | `prest/regTrib/opSimpNac = 3` × perfil `Regime tributário = Simples Nacional - …`; `regApTribSN = 1`; `regEspTrib = 0`; `tribISSQN = 1`; `tpRetISSQN = 1` | "recolhimento mensal, mediante documento único de arrecadação" |
| nfse-05.xml | 5-aritmética · as contas da nota (serviço, deduções, retenções, líquido) | LC116 art. 7 | PASSA | — | `vLiq 290,00` = `vServ 290,00` − 0,00 (deduções) − 0,00 (retenções; `tpRetISSQN = 1`) | "A base de cálculo do imposto é o preço do serviço." |
| nfse-05.xml | 5-alíquota · alíquota de ISS que a nota mostra | LC123 art. 13 | NÃO SE APLICA | — | `pAliqAplic ausente; vISSQN/vBC = 14,50/290,00 = 5,00% (informativo)`; para optante do Simples a tabela municipal não é a aplicável (ISS no DAS) | "recolhimento mensal, mediante documento único de arrecadação" |
| nfse-05.xml | 6 · IBS e CBS | LC214 art. 62 | NÃO SE APLICA | — | grupo `IBSCBS`/`CST`/`cClassTrib` ausente | "os Municípios e o Distrito Federal ficam obrigados, a partir de 1º de janeiro de 2026" |

Não lidos: nenhum.

**The FAIL here was not planted.** In `fixtures/mutations/` the author changed one field on purpose and wrote down which one. Nothing was changed here but the identifiers: the note left the client's own system carrying `cTribNac` 31.01 while the office's sheet registers item 7.02 for that client. Which of the two is right is the office's question to its client, and it is still open (`../rounds/round-2-v2/what-changed.md`). This file does not answer it. It says what the audit must return given the note and the sheet, which is a FAIL that hands the decision back.
