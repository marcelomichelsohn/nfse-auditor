Variant V3 (new vocabulary, short location) — assembled 10/09/2026 from the round-1 note (`rounds/round-1-v1/transcript.md`), with placeholders, for the author to compare formats; it is not a round and not a new report.

**Totais para a sua comparação:** competência 08/2026 (`dCompet` = 2026-08-07) → soma de `vServ` = **R$ […]** (1 nota lida).

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nNFSe 2026000000008 | 1-código · código de serviço da nota comparado com o item do cadastro | LC116 art. 1 | FALHA | corrigir antes de fechar · você decide antes de fechar | `DPS/infDPS/serv/cServ/cTribNac = 310101` | como fato gerador a prestação de serviços constantes da lista anexa |
| nNFSe 2026000000008 | 1-descrição · descrição escrita pelo cliente comparada com o nome do serviço do código | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | `DPS/infDPS/serv/cServ/xDescServ = "[descrição livre do serviço, na nota]"` | A incidência do imposto não depende da denominação dada ao serviço prestado. |
| nNFSe 2026000000008 | 2 · campos obrigatórios do leiaute nacional | required-fields.md (ANEXO I / XSD v1.01) | PASSA | — | (todos os obrigatórios presentes) | Valor líquido da NFS-e. |
| nNFSe 2026000000008 | 3 · município onde o ISS é devido | LC116 art. 3 | PASSA | — | `infNFSe/cLocIncid = 2800308`; `DPS/infDPS/cLocEmi = 2800308` | O serviço considera-se prestado, e o imposto, devido, no local do estabelecimento prestador |
| nNFSe 2026000000008 | 4 · marcações do Simples Nacional comparadas com o regime do cadastro | LC123 art. 13 | PASSA | — | `prest/regTrib/opSimpNac = 3` | mediante documento único de arrecadação, |
| nNFSe 2026000000008 | 5-aritmética · as contas da nota (serviço, deduções, retenções, líquido) | LC116 art. 7 | PASSA | — | `vLiq = […]` | A base de cálculo do imposto é o preço do serviço. |
| nNFSe 2026000000008 | 5-alíquota · alíquota de ISS que a nota mostra | LC123 art. 13 | NÃO SE APLICA | — | `pAliqAplic` = (ausente) | mediante documento único de arrecadação, |
| nNFSe 2026000000008 | 6 · IBS e CBS | LC214 art. 62 | NÃO SE APLICA | — | `CST`/`cClassTrib` = (ausente) | os Municípios e o Distrito Federal ficam obrigados, a partir de 1º de janeiro de 2026 |

**Não lidos:** nenhum — o arquivo `[código do município + CNPJ do emitente + número da nota].xml` é NFS-e de padrão nacional (raiz `NFSe` v1.01 com `DPS` embutida) e foi auditado.
