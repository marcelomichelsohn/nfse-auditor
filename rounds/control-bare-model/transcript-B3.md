# Bare model, run B3 — `nfse-01.xml` (clean) + profile line, plain chat, no folder, the stronger model (2026-09-09 ~14:15)

**Conditions:** Claude Fable 5.1, effort "high"; a plain conversation outside any project, **web search on**; the XML attached, the profile line and the fixed request of `expected.md` pasted. After the review the operator typed "continue" once; the model then wrote a validator script (493 lines, kept outside this folder by the author). Kept as it came; the app's own tool-use lines ("Searched the web, ran 2 commands…") are part of what the operator saw.
**What happened, in one line:** the widest review of the three bare runs — everything B1 found, plus real things the folder does not check (the anonymised `Id` attributes do not follow the layout's numeric format; the "alíquota do Simples" label; the IBPT figures incoherent with each other; `pAliqAplic` absent; leading zeros; no signature; an emission-channel deadline taken from a CGSN resolution found on the web) — with corrections advised throughout, and then a tool that reproduces its own verdicts.

---

**Operator:** *(attaches `nfse-01.xml`)*
perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não
Confira esta nota fiscal de serviço (NFS-e) contra as normas que se aplicam a ela: a lei do ISS, o Simples Nacional e o leiaute nacional da NFS-e. Diga o que passa e o que falha, onde, e cite a norma. A linha "perfil" é o cadastro do cliente.

**Model:**

Searched the web, ran 2 commands, and 2 more tools
Li o XML. Resumo: a nota está bem montada no que depende da LC 116 (enquadramento, local de incidência, retenção, base, alíquota mínima), mas tem uma contradição de fundo com o cadastro — declara o ISS apurado dentro do Simples e calcula ISS ad valorem para um escritório contábil que o próprio texto da nota chama de "Fixo Contador" — e os identificadores da NFS-e/DPS não respeitam o formato do leiaute.

O que passa

Serviço: cTribNac 171901 = item 17.19 da lista anexa à LC 116/2003 ("Contabilidade, inclusive serviços técnicos e auxiliares"); xTribNac reproduz o texto legal; coerente com CNAE 6920-6/01 e com o item 17.19 do perfil.
Local de incidência: LC 116, art. 3º, caput — ISS devido no estabelecimento prestador; 17.19 não está entre as exceções dos incisos I a XXV. cLocIncid = cLocEmi = cMun do emitente = 2800308 (Aracaju). O tomador em Barueri (3505708) não desloca a incidência. A regra do leiaute confirma: para códigos fora da lista de exceções, a localidade de incidência é o município do endereço do prestador.
Retenção: tpRetISSQN = 1 (não retido) — correto. LC 116, art. 6º, §2º só atribui responsabilidade ao tomador nos serviços do art. 3º; LC 123, art. 21, §4º só admite retenção de optante observado o art. 3º da LC 116. Tomador de outro município não reteria ISS devido a Aracaju.
Base e alíquota: LC 116, art. 7º (preço do serviço) → vBC = vServ = 400,00, vCalcDR 0,00, vLiq 400,00 (nada retido). Alíquota efetiva 8/400 = 2%: respeita o piso do art. 8º-A e o teto de 5% do art. 8º, II. O leiaute também exige que a base não resulte em alíquota efetiva menor que 2%.
Simples: opSimpNac = 3 (ME/EPP) coerente com "Simples optante"; cStat 100 (não 107, que é MEI).
Exportação: tribISSQN = 1, sem grupo comExt — coerente com "exporta não" (LC 116, art. 2º, I não se aplica).
Datas: dCompet 2026-08-31 ≤ dhEmi 2026-09-02; competência é a data do fato gerador (LC 116, art. 1º). Grupo IBS/CBS não exigível para esta competência (obrigatório só para notas com competência superior a 01/10/2026).
Canal de emissão: tpEmis 2 + ambGer 1 + verAplic Abrasf_202 = emitida no sistema próprio de Aracaju e transcrita. Hoje passa: a Res. CGSN 189/2026 obrigaria ME/EPP a usar o Emissor Nacional (web ou API) a partir de 1º/09/2026, mas foi revogada e o prazo passou para 1º de novembro de 2026 (Res. CGSN 191/2026). A partir de 1º/11 esse caminho de emissão falha (Res. CGSN 140, art. 59, §1º, nova redação). 
Resolução CGSN Nº 189 DE 23/04/2026 +2
Lei 12.741/2012, art. 1º: valores aproximados por ente e fonte (IBPT) constam na descrição, em xOutInf e em vTotTrib. Formalmente atendido (ver falha 4 quanto à coerência).
Cadastrais: CNPJs do prestador e tomador com dígitos verificadores válidos; tomador PJ com CNPJ e endereço completo; endereço do emitente completo.
O que falha

Regime de apuração do ISS × ISS fixo — risco alto, confiança alta. Onde: prest/regTrib/regApTribSN = 1 e regEspTrib = 0; consequência em infNFSe/valores/vISSQN = 8,00. Norma: LC 123, art. 18, §22-A — a atividade do inciso XIV do §5º-B (escritórios de serviços contábeis) "recolherá o ISS em valor fixo, na forma da legislação municipal"; no PGDAS-D o percentual de ISS é desconsiderado (Res. CGSN 140, art. 25, na redação que herdou a Res. 107/2013). O código 1 significa apuração dos tributos federais e municipal pelo SN; o 2, federais pelo SN e ISSQN conforme a legislação municipal. A nota diz duas coisas incompatíveis: "Fixo Contador" no xOutInf e "ISS dentro do DAS" no regApTribSN, e por isso o sistema calculou R$ 8,00 de ISS sobre esta operação, valor que não será pago nem pelo DAS (o ISS está fora dele) nem pela guia fixa (que independe do faturamento). Exposição: do prestador — divergência NFS-e × PGDAS-D e risco de o município cobrar os 8,00 "destacados". Correção: regApTribSN = 2; e, para o ADN não calcular ISS, enquadrar o regime fixo em regEspTrib conforme a parametrização de Aracaju (o leiaute só deixa de calcular o ISSQN quando o prestador tem um regime especial de tributação; o catálogo traz "6 – Sociedade de Profissionais", mas o código exato depende do cadastro municipal — confiança média nesse ponto). Ressalva: se Aracaju não autoriza o fixo para este contribuinte (hipótese do art. 25, §3º da Res. 140), então o erro está no perfil ("anexo fixo"), e regApTribSN = 1 estaria certo — vale confirmar no cadastro municipal antes de corrigir.
Identificadores fora do formato — risco alto (integridade/chave de acesso), confiança alta. Onde: infNFSe/@Id = NFS21F0911121F09… e infDPS/@Id = DPS8079D62E…. O Id da NFS-e é "NFS" + 50 posições: código do município (7), ambiente gerador (1), tipo de inscrição (1), inscrição federal (14), nNFSe (13), ano-mês da DPS (4), código numérico (9) e DV (1); o da DPS é "DPS" + 42 posições numéricas: município (7), tipo de inscrição (1), inscrição (14), série (5) e número da DPS (15). Os dois têm o tamanho certo (53 e 45) mas contêm letras e não começam por 2800308. Esperado: NFS 2800308 1 2 99000000000159 0000000000001 2609 + 9 dígitos + DV e DPS 2800308 2 99000000000159 26000 000000000000001. Isso reprova no XSD; se o arquivo foi anonimizado, é só ruído — se é o XML de produção, a chave da nota está inválida.
Alíquota rotulada como "alíquota do Simples" — risco médio, confiança alta. Onde: xOutInf ("Alíquota do Simples Nacional: 2,0000%"). 2% é, no máximo, a parcela de ISS da 1ª faixa do Anexo III (6% × 33,5% = 2,01%) ou o piso municipal — não é a alíquota do Simples, e num regime de ISS fixo não é alíquota nenhuma. Reforça a contradição da falha 1. Correção: remover a frase ou substituir pela informação do regime fixo.
Tributos aproximados incoerentes entre si — risco baixo, confiança alta. Onde: vTotTribMun 20,00 (5%) contra vISSQN 8,00 (2%); vTotTribFed 53,80 (13,45%) incompatível com Anexo III na 1ª faixa (≈3,99% federal ≈ R$ 15,96). A Lei 12.741 admite valor aproximado, então não é infração — mas o documento informa três números municipais diferentes (5%, 2% e fixo). Exposição: do tomador, mínima. Correção: usar pTotTribSN ou alinhar a tabela IBPT ao regime.
pAliqAplic ausente em infNFSe/valores embora vISSQN tenha sido calculado — risco baixo, confiança média (depende da ocorrência no XSD da versão; se opcional, é só perda de rastreabilidade).
Zeros não significativos em nNFSe, nDPS e nDFSe — risco baixo, confiança média. O manual pede que não se incluam zeros não significativos em campos numéricos; alguns ambientes toleram.
Sem Signature e dados obviamente fictícios (fone 0000000000, e-mail .invalid) — observação. Passam no schema, mas uma NFS-e gerada pelo município deveria vir assinada pela administração tributária; se este é o arquivo oficial, falta a assinatura.
Sobre o art. 59 da Res. CGSN 140 (expressões "documento emitido por ME/EPP optante…"): no padrão nacional a condição é carregada por opSimpNac, então trato como não aplicável — confiança baixa, porque não confirmei a redação vigente após as Res. 190/191.

Se quiser, o próximo passo é eu converter essas regras num validador (perfil + XML → passa/falha com a norma), já que você vai repetir isso para outros clientes.

**Operator:** continue

**Model:**

Thought for 19s
Fechado — vou montar o validador: perfil + XML → passa/falha/aviso, cada achado com onde, norma, risco e confiança, seguindo exatamente os pontos que apliquei acima.

Ran 2 commands, created a file, read a file
Rodei o validador na nfse-01.xml com o seu perfil e ele reproduz o parecer: 5 falhas (os dois Ids fora do formato; regApTribSN = 1, regEspTrib = 0 e vISSQN 8,00 contra o ISS fixo), 7 avisos (rótulo "alíquota do Simples", IBPT incoerente, pAliqAplic ausente, zeros à esquerda, sem assinatura, emissão por sistema municipal com prazo de 1º/11/2026) e 14 checagens ok.

Uso: python3 nfse_check.py nota.xml "CNAE …; regime …; anexo …; município …; item LC 116 …; exporta …" (ou --perfil arquivo.txt; --json para integrar). Sai com código 1 se houver falha. Cada achado traz código, resultado, risco/confiança, caminho no XML, norma e correção.

O que está codificado: enquadramento item×CNAE (tabela pequena, CNAE_ITENS — amplie com a carteira), incidência pelas listas do leiaute (art. 3º da LC 116), retenção, base/alíquota efetiva/líquido, situação no Simples, ISS fixo, exportação, datas, canal de emissão, formato e coerência dos Ids, DV de CNPJ/CPF, Lei 12.741, IBS/CBS por competência e assinatura. Testei também um perfil divergente (outro município, item 17.20, exporta sim) para confirmar que os ramos contrários disparam.

Limites que valem saber: as tabelas de exceção vieram do manual v1.01 (rev. 03/08/2026) e as datas-limite (1º/11 emissor nacional, 1º/10 IBS/CBS) estão como constantes no topo do arquivo; o código não valida contra o XSD nem consulta a parametrização municipal do ADN — aquela dúvida sobre qual regEspTrib Aracaju usa continua manual.
