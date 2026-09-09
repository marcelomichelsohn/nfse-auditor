# Bare model, run B1 — `nfse-01.xml` (clean) + profile line, plain chat, no folder (2026-09-09 ~13:25)

**Conditions:** Claude Opus 4.8, effort "low"; a plain conversation outside any project; the XML attached, the profile line pasted, the fixed request of `expected.md`; **4 min 50 s** by the author's clock. *(Whether web search was on in that chat: see the note at the end.)* Kept as it came.

---

**Operator:** *(attaches `nfse-01.xml`, pastes the profile line and the request of `expected.md`)*

**Model:**

Conferido o XML contra as três normas. Resumo do veredito: a **incidência territorial está correta**, mas o **enquadramento do ISS está inconsistente com o cadastro "anexo fixo"** — a nota recolhe o ISS como percentual dentro do Simples, e não em valor fixo. Detalho o que falha e o que passa, com o "onde" (tag do XML), a norma e a classificação de risco/confiança.

---

## O que FALHA

**1. ISS apurado dentro do Simples (2%) em vez de valor fixo**
*Onde:* `DPS/infDPS/prest/regTrib/regApTribSN = 1` e, como consequência, `infNFSe/valores/vBC = 400,00` com `vISSQN = 8,00` (2%). O `xOutInf` confirma: "Alíquota do Simples Nacional: 2,0000%".

No leiaute nacional, `regApTribSN = 1` significa "apuração dos tributos federais **e municipal** pelo Simples Nacional" — ou seja, o ISS entra no DAS como percentual. A regra de negócio do Anexo I (Leiautes e RN da DPS/NFS-e, SE/CGNFS-e) é explícita: uma ME/EPP deixa de apurar o ISSQN pelo Simples Nacional quando atribui ao campo regApTribSN os valores 2 ou 3. Para contador optante que recolhe fixo, o correto é **`regApTribSN = 2`** (federais pelo SN, ISS por fora, pela legislação municipal).

A base legal do fixo é a LC 123/2006, art. 18, § 22-A c/c § 5º-B, XIV: a atividade constante do inciso XIV do § 5º-B deste artigo recolherá o ISS em valor fixo, na forma da legislação municipal (o inciso XIV são os escritórios de serviços contábeis). E o efeito prático, confirmado pela orientação do CGSN: nesta hipótese o ISS não será contemplado no PGDAS. Aqui ele está sendo contemplado — logo, contradiz o cadastro "anexo fixo".

- **Risco: alto** · **Confiança: alta** (na regra de leiaute e na lei) / **média** (na aplicação ao caso concreto — depende do item de verificação abaixo).
- **Parte afetada:** a direção depende do valor fixo municipal frente ao faturamento. Se o fixo de Aracaju for menor que 2% do movimento mensal, a nota **prejudica o contribuinte** (recolhe ISS a mais); se for maior, **prejudica o Fisco**. Em qualquer cenário, expõe o prestador a retificação/autuação por regime declarado errado.
- **Correção:** `regApTribSN` → `2`; ISS deixa de sair no DAS e passa a ser recolhido em guia municipal (DAM) em valor fixo. `vISSQN` na nota deixa de refletir os 2% apurados pelo SN.

**2. Regime especial de tributação não sinalizado**
*Onde:* `DPS/infDPS/prest/regTrib/regEspTrib = 0` (Nenhum).

Para PJ com recolhimento de ISS fixo — o exemplo típico é o escritório de contabilidade — o leiaute nacional prevê `regEspTrib = 6` (Sociedade de Profissionais). A orientação oficial de BH/CRC-MG lista o código 6 – Sociedade de Profissionais, destinado às Sociedades de Profissionais Liberais, e a documentação de integração ao emissor nacional é direta: pessoas jurídicas com regime de recolhimento de ISS Fixo — exemplo: escritório de contabilidade — devem enviar a tag regEspTrib com o valor 6.

- **Risco: médio** · **Confiança: média** (a exigência de `regEspTrib = 6` combinada com optante do Simples pode variar conforme a parametrização do município de incidência; alguns validam, outros esperam que o fixo venha só pelo `regApTribSN`).
- **Parte afetada:** o contribuinte — a omissão descaracteriza documentalmente o enquadramento uniprofissional/fixo e pode gerar rejeição ("Regime especial não permitido para o prestador…") ou tributação como serviço comum.
- **Correção:** `regEspTrib` → `6`, alinhado ao `regApTribSN = 2`.

**3. Base de cálculo e valor do ISS preenchidos como operação comum**
*Onde:* `infNFSe/valores/vBC = 400,00` e `vISSQN = 8,00`.

É sintoma dos itens 1 e 2: no fixo, o ISS não se calcula sobre o valor do serviço da nota. Corrigidos o `regApTribSN` e o `regEspTrib`, esses campos deixam de expressar 2% sobre R$ 400.

- **Risco: médio** · **Confiança: alta** (é decorrência aritmética dos itens acima). **Parte afetada:** contribuinte.

---

## O que PASSA

**Município de incidência (o ponto mais sensível, e está certo).** `infNFSe/cLocIncid = 2800308` (Aracaju), igual ao estabelecimento do prestador, mesmo com o tomador em Barueri/SP (`toma/end/endNac/cMun = 3505708`). Contabilidade (17.19) **não** está entre as exceções dos incisos I–XXV do art. 3º da LC 116/2003, então vale a regra geral: ISS devido no estabelecimento prestador. A nota **não** deslocou a incidência para o tomador — correto. · *Risco de erro: nenhum · Confiança: alta.*

**Código do serviço.** `cServ/cTribNac = 171901` mapeia o subitem 17.19 da LC 116, e o `xTribNac`/`xTribMun` trazem "Contabilidade, inclusive serviços técnicos e auxiliares" — consistente com o perfil (CNAE 6920-6/01, LC 116 17.19). · *Confiança: alta.*

**Situação no Simples.** `regTrib/opSimpNac = 3` (Optante ME/EPP) bate com o cadastro "Simples optante". · *Confiança: alta.*

**Tributação/retenção do ISS.** `tribISSQN = 1` (operação tributável) é coerente com "exporta não". `tpRetISSQN = 1` (não retido) é coerente — sendo o ISS devido em Aracaju, o tomador em Barueri não retém. A própria regra do emissor nacional: tribISSQN com valor 1 e tpRetISSQN com valor 1 será considerado como imposto retido "Não". · *Confiança: alta.*

**Coerência de valores.** `vServ = vBC = vLiq = 400,00`, sem deduções (`vCalcDR = 0,00`). Íntegro na aritmética (a ressalva é só o `vISSQN`, tratado acima). Os R$ 53,80 federais e R$ 20,00 municipais no `xOutInf`/`totTrib` são o **IBPT aproximado** (Lei 12.741/2012, transparência), meramente informativo — não é o ISS real, então a divergência entre os R$ 20 do IBPT e os R$ 8 da nota não é, em si, um erro.

---

## O que precisa ser verificado para fechar o diagnóstico

A contradição toda gira em torno de **um fato de direito municipal que eu não consigo confirmar daqui**: a legislação de Aracaju concede (e este contador se enquadra em) o ISS em **valor fixo**?

O que consegui verificar do Código Tributário de Aracaju: ele fixa a alíquota mínima do ISS em 2% (art. 103-A) e tem um regime de sociedade uniprofissional com critérios de exclusão (sócio não habilitado, sócio só de capital, existência de filial etc.). Ou seja, os 2% da nota são exatamente o **mínimo comum** de Aracaju — o que reforça que a nota foi emitida como serviço comum, não como fixo.

Duas leituras honestas:

- **Se o cadastro "anexo fixo" está correto** (Aracaju autoriza o fixo e o escritório cumpre os requisitos personalíssimos — a jurisprudência recente do STJ, REsp 2.162.486/SP, admite até LTDA desde que preste serviço pessoal, sem estrutura empresarial): então a **nota está errada** nos itens 1–3 e deve ser retificada.
- **Se Aracaju é omissa/não autoriza o fixo para este caso**: aí a nota está certa (ISS pelo Anexo III no DAS, art. 25, § 1º, III da Resolução CGSN 140/2018) e é o **cadastro "anexo fixo" que está errado**.

De um jeito ou de outro, cadastro e nota estão dizendo coisas diferentes, e isso tem que ser reconciliado.

Se quiser, puxo o artigo específico do CTM de Aracaju sobre sociedades uniprofissionais/contadores e a lei que estipula o valor fixo, para cravar qual das duas leituras vale — é o que decide se corrigimos a nota ou o cadastro.
