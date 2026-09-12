# nfse-auditor

**A note on languages.** This file carries the instructions twice: in Portuguese for the operator at the accounting firm, and in English for everyone else. That makes it longer than most.

**What this is.** An instruction folder that turns an LLM into an auditor of Brazilian electronic service invoices (NFS-e). You give it one invoice and one line with your client's information. It returns one row per check per invoice, naming the provision word for word, and giving the value it read in the invoice. It doesn't correct, decide or guess.

**What comes back.** Two rows from a recorded run, copied exactly as the folder returned them. The columns are: invoice, check, which provision, result, severity, where it was found, and the provision's exact words. The four complete audits are in [`examples.md`](https://github.com/marcelomichelsohn/nfse-auditor/blob/main/examples.md).

| nota | check | dispositivo | resultado | severidade | localização | trecho citado |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-código | LC116 list item 17 | PASSA | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` (item 17.19; perfil `item LC 116 = 17.19`; código consta na ANEXO_B) | 17.19 – Contabilidade, inclusive serviços técnicos e auxiliares. |
| nfse-01.xml | 1-descrição | LC116 art. 1 | NÃO DÁ PARA DETERMINAR | — | `xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares."` × `DPS/infDPS/serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 ..."` — coincidência entre o texto livre e o código é juízo, não mecânica | A incidência do imposto não depende da denominação dada ao serviço prestado. |

The second row is the one that matters most: when a check needs a fact about the client that the folder was not given, the folder says which fact is missing.

**Three places where it stops instead of guessing:** without the client's line, the checks that need it return "cannot determine"; a file that is not national-standard XML goes under "Not read"; a request for a decision is handed back. What each one does, and the full list of what this auditor does not check, are [`rules.md`](https://github.com/marcelomichelsohn/nfse-auditor/blob/main/rules.md) § 4 and § 5.

**What is behind it.** Each row points to something in this repository a reader opens to check a claim on this page.

| | |
|---|---|
| The law it cites, in full, in Portuguese and in English, each file with its SHA-256 beside it | [`reference/`](https://github.com/marcelomichelsohn/nfse-auditor/tree/main/reference) |
| The recorded rounds with a real accounting office, and a session in which someone from outside the trade ran the folder alone | [`rounds/`](https://github.com/marcelomichelsohn/nfse-auditor/tree/main/rounds) |
| What the folder must return on each test invoice. The author's own were committed before the run, which `prove_order.py` checks in a fresh clone; the four for the office's real invoices were written **after** the office had already audited them, and are gabaritos (answer keys), not predictions | [`expected/`](https://github.com/marcelomichelsohn/nfse-auditor/tree/main/expected) |
| The commands that check the claims on this page, each one saying what it does not cover | [`tools/`](https://github.com/marcelomichelsohn/nfse-auditor/tree/main/tools) |
| The four questions of the competition brief, answered one by one | [`BRIEF.md`](https://github.com/marcelomichelsohn/nfse-auditor/blob/main/BRIEF.md) |


## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação, ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Baixe a pasta do auditor: [nfse-auditor-carregar.zip](https://github.com/marcelomichelsohn/nfse-auditor/raw/main/download/nfse-auditor-carregar.zip).
2. Descompacte o arquivo baixado.
3. Na pasta descompactada, ache o arquivo chamado `CLAUDE.md` (o Windows pode mostrar só `CLAUDE`, sem o `.md`). Clique nele com o botão direito e escolha Abrir com › Bloco de Notas, que é o editor de texto do Windows; em outro sistema, qualquer editor de texto simples serve.
4. Selecione tudo e copie.
5. No app do Claude, no menu da esquerda, clique em "Projetos".
6. Crie um projeto novo com o nome `nfse-auditor` (se já existir um com esse nome, use outro nome).
7. Deixe o campo "Pasta" vazio.
8. No projeto, no painel da direita, em "Instruções" (não é uma conversa), cole o que copiou e salve.
9. No mesmo painel, em "Contexto", adicione todos os outros arquivos da pasta descompactada, selecionando todos de uma vez.

**Como usar:**

10. Dentro do projeto, comece uma conversa nova.
11. Na caixa de mensagem, deixe marcado "Chat", não "Cowork".
12. Ao lado da caixa de mensagem, clique no nome do modelo.
13. Abra a lista completa de modelos e escolha "Opus 4.8".
14. Escolha o esforço "Baixo".
15. Anexe um só arquivo XML de nota fiscal do padrão nacional por conversa. Uma nota por conversa porque a conversa guarda o que já leu: se você anexar uma segunda nota na mesma conversa, ela é conferida junto com a primeira e com os dados que você já tinha digitado, e o resultado deixa de valer só para ela. Começar uma conversa nova demora um pouco mais, porque o sistema lê a pasta de novo. Vale a espera: é assim que cada nota é conferida sozinha.
16. Na mensagem vão o regime tributário do cliente, o Anexo e o Código de Atividade. Copie o exemplo a seguir, cole na mensagem e troque os valores pelos do seu cliente, tirados da sua planilha ou do seu cadastro: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (se tiver mais de um código, digite todos).
17. Envie.

**O sistema responderá com:**

1. a soma do `vServ` das notas lidas, por mês de competência (`dCompet`) — que não é o total da nota quando há deduções ou retenções;
2. uma tabela que audita os dados da nota comparando com as legislações vigentes e te avisa se a verificação PASSA, FALHA, NÃO DÁ PARA DETERMINAR ou NÃO SE APLICA;
3. um aviso de "Não lidos" caso o arquivo anexado não seja reconhecido como uma nota pelo sistema;
4. um bloco de texto CSV caso você queira criar um arquivo que possa ser aberto no Excel para facilitar sua conferência.

Os nomes entre aspas são os da tela do app em português, vistos em 09/09/2026; versões novas do app podem mudá-los.

**Três situações em que ela para em vez de adivinhar:** sem a linha do passo 16, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo) entra em "Não lidos"; um pedido de decisão ("qual item eu uso?") volta para você, com a nota e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**Set-up, once:**

1. Download the auditor's folder: [nfse-auditor-carregar.zip](https://github.com/marcelomichelsohn/nfse-auditor/raw/main/download/nfse-auditor-carregar.zip).
2. Unpack the downloaded file.
3. In the unpacked folder, find the file named `CLAUDE.md` (Windows may show it as `CLAUDE`, without the `.md`). Right-click it and choose Open with › Notepad.
4. Select all and copy.
5. In the Claude app, in the left menu, open the projects list.
6. Create a new project named `nfse-auditor` (if one with that name already exists, use another name).
7. Leave the project's folder field empty.
8. In the project, in the right-hand panel, paste what you copied into the project's own instructions field (not a conversation) and save.
9. Under the project's context, add every other file of the unpacked folder, selecting them all at once.

**Use:**

10. Inside the project, start a new conversation.
11. In the message box, keep "Chat" selected, not "Cowork".
12. Beside the message box, click the model's name.
13. Open the full list of models and choose "Opus 4.8".
14. Set the effort to low.
15. Attach one national-standard NFS-e XML file per conversation, and only one. One invoice per conversation because the conversation keeps what it has already read: if you attach a second invoice to the same conversation, it is audited together with the first and with the data you had already typed, and the result no longer applies to it alone. Starting a new conversation takes a little longer, because the folder is read again. It is worth the wait: that is what keeps each invoice audited on its own.
16. The message carries the client's tax regime, the Anexo and the Código de Atividade. Copy the example that follows, paste it into the message and replace its values with your client's, taken from your spreadsheet or your client record: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (if there is more than one code, type them all).
17. Send.

**The system answers with:**

1. the sum of `vServ` over the invoices read, by reference month (`dCompet`) — which is not the invoice's total when there are deductions or withholdings;
2. a table that audits the invoice's data against the legislation in force and tells you whether each check is PASS, FAIL, CANNOT DETERMINE or NOT APPLICABLE;
3. a "Not read" notice if the attached file is not recognised as an invoice by the system;
4. a CSV text block, in case you want to make a file that opens in Excel to make your checking easier.

The names in quotes are the labels of the app's Portuguese screen, seen on 09/09/2026, plus the names that are the same in any language (Chat, Cowork, Opus 4.8); new versions of the app may change them. The other fields are named by what they do.

## What to load, and what never to load
What to load: the files the operator's folder contains, and nothing else. `identity.md` · `rules.md` · `output-contract.md` · `examples.md` · `README.md` · `reference/INDEX.md` · `reference/pt/excerpts/` · `reference/en/excerpts/` · `reference/tables/required-fields.md` · `reference/tables/TABLES.md` · `reference/tables/working/` · `reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` · `reference/tables/official/csv/`; `CLAUDE.md` goes into the project's instructions.
Never load: `fixtures/` · `expected/` · `rounds/` · `tools/` · `reference/pt/full/` · `reference/en/full/`. They exist to check the auditor; they are not part of it.

The operator receives the loaded files copied flat into one folder: the zip in `download/`, built from the list above by the script `make_load_folder.py`. That list resolves to two files more than the zip carries, because the two `SHA256SUMS.txt` under `reference/tables/` are there for a reader checking a hash and are not loaded.

## How to check it
The test invoices themselves are in `fixtures/`: anonymised invoices of the author's own company, four real ones of a client of the office carrying a real wrong-code FAIL, one-field mutations with a `CHANGE.md` saying what was changed and which check must catch it, and one violation kept while the text around it is reworded three ways.

**Measured against the model alone** (`rounds/control-bare-model/`): given the same invoices with no folder and web search on, the model alone covers more of the law than these checks do. Four things it never did, in any run: give a citation that can be checked offline; stop where a fact was missing; hand the decision back; return the same structure twice. Those four are what this folder is for, and the folder did them in every run recorded in `examples.md`, on Claude Opus 4.8 at low effort. What each run proves and does not prove: `rounds/control-bare-model/what-this-shows.md`.

**Who the witness is.** A real accounting firm, in operation. It provides accounting services to the author: the relationship is commercial and predates this competition. There is no personal relationship with anyone there. The office is also a potential client of the product. The rounds run inside its working routine, on invoices of its real clients, under the conditions in `rounds/CONSENT.md`; roles, never names (`rounds/README.md` § Roles).

**Dates in this repository are written day/month/year**, the Brazilian order: `11/09/2026` is the eleventh of September, not the ninth of November.

**"Note" and "invoice" mean the same thing here**: both render the Portuguese *nota fiscal*. The recorded rounds, the reports and the predictions say "note" throughout; this page says "invoice".

**How it was built.** With Claude, in the open: the request for the first round is the first commit; predictions precede reports; nothing in a report was edited after the run. This README was rewritten and measured on 11/09/2026, after round 1: the rewrite took the whole file from 1813 words at commit `6035cb9` to 1530 at commit `a4a2233`, and the Portuguese step-by-step from 470 to 513, because seven vague instructions became seventeen commands (the method is in `rounds/round-1-v1/what-changed.md`). Those two numbers belong to those two commits and stay true there. The file has grown since, as each round and walk added a paragraph of its own, and the last pass before submission replaced the opening and put an example of the output on the first screen; `wc -w README.md` gives today's figure, and this sentence does not repeat it, because a number written into prose is false the next time someone edits the file. The version the office received for round 1 is at commit `ac96786`.
