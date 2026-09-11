# nfse-auditor

As instruções de uso vêm duas vezes: primeiro em português, para quem vai usar a pasta no escritório; depois em inglês. As duas dizem a mesma coisa; o resto do arquivo está só em inglês.

The instructions come twice: first in Portuguese, for the person who will use the folder at the accounting office in Brazil; then in English. The two say the same thing; the rest of this file is in English only.

## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação, ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Baixe a pasta do auditor: [nfse-auditor-carregar.zip](https://github.com/marcelomichelsohn/nfse-auditor/raw/main/download/nfse-auditor-carregar.zip).
2. Descompacte o arquivo baixado.
3. Abra o arquivo `CLAUDE.md` da pasta descompactada com o Bloco de Notas.
4. Selecione tudo e copie.
5. No app do Claude, no menu da esquerda, clique em "Projetos".
6. Crie um projeto novo com o nome `nfse-auditor` (se já existir um com esse nome, use outro nome).
7. Deixe o campo "Pasta" vazio.
8. No projeto, no painel da direita, em "Instruções", cole o que copiou e salve.
9. No mesmo painel, em "Contexto", adicione todos os outros arquivos da pasta descompactada, selecionando todos de uma vez.

**Como usar:**

10. Dentro do projeto, comece uma conversa nova.
11. Na caixa de mensagem, deixe marcado "Chat", não "Cowork".
12. Ao lado da caixa de mensagem, clique no nome do modelo.
13. Abra a lista completa de modelos e escolha "Opus 4.8".
14. Escolha o esforço "Baixo".
15. Anexe um só arquivo XML de nota fiscal do padrão nacional por conversa.
16. Digite na mensagem o regime tributário do cliente, o Anexo e o Código de Atividade, neste formato: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (se tiver mais de um código, digite todos). Se você tiver uma planilha ou sistema com esses dados, copie e cole na mensagem.
17. Envie.

**O sistema responderá com:**

1. o total da nota;
2. uma tabela que audita os dados da nota comparando com as legislações vigentes e te avisa se a verificação PASSA, FALHA, NÃO DÁ PARA DETERMINAR ou NÃO SE APLICA;
3. um aviso de "Não lidos" caso o arquivo anexado não seja reconhecido como uma nota pelo sistema;
4. um bloco de texto CSV caso você queira criar um arquivo que possa ser aberto no Excel para facilitar sua conferência.

Os nomes entre aspas são os da tela do app em português, vistos em 09/09/2026; versões novas do app podem mudá-los.

**Três situações em que ela para em vez de adivinhar:** sem a linha do passo 16, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo) entra em "Não lidos"; um pedido de decisão ("qual item eu uso?") volta para você, com a nota e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**What it is.** A folder that audits Brazilian service invoices (NFS-e, national standard) under the ISS law, the Simples Nacional and the national layout. For each note and each check it returns pass / fail / cannot determine / not applicable, with the provision quoted verbatim. It corrects nothing and decides nothing for you.

**Set-up, once:**

1. Download the auditor's folder: [nfse-auditor-carregar.zip](https://github.com/marcelomichelsohn/nfse-auditor/raw/main/download/nfse-auditor-carregar.zip).
2. Unpack the downloaded file.
3. Open the unpacked folder's `CLAUDE.md` with Notepad.
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
15. Attach one national-standard NFS-e XML file per conversation, and only one.
16. In the message, type the client's tax regime, the Anexo and the Código de Atividade, in this form: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (if there is more than one code, type them all). If you have a spreadsheet or a system with these data, copy and paste them into the message.
17. Send.

**The system answers with:**

1. the note's total;
2. a table that audits the note's data against the legislation in force and tells you whether each check is PASS, FAIL, CANNOT DETERMINE or NOT APPLICABLE;
3. a "Not read" notice if the attached file is not recognised as a note by the system;
4. a CSV text block, in case you want to make a file that opens in Excel to make your checking easier.

The names in quotes are the labels of the app's Portuguese screen, seen on 09/09/2026, plus the names that are the same in any language (Chat, Cowork, Opus 4.8); new versions of the app may change them. The other fields are named by what they do.

**Three situations where it stops instead of guessing:** without the line of step 16, the checks that need it return "cannot determine"; a file that is not national-standard XML (a municipality's own, for instance) goes under "Not read"; a request for a decision ("which item should I use?") is handed back, with the note and the rule beside it.

**What it does not do:** it does not fetch notes, compute the monthly tax (DAS), compare the client's declared revenue with the notes (it only sums the notes for you to compare), read a municipality's own XML or a PDF, validate the digital signature, or decide anything for you.

## What to load, and what never to load
What to load: the files the operator's folder contains, and nothing else. `identity.md` · `rules.md` · `examples.md` · `README.md` · `reference/INDEX.md` · `reference/pt/excerpts/` · `reference/en/excerpts/` · `reference/tables/required-fields.md` · `reference/tables/TABLES.md` · `reference/tables/working/` · `reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` · `reference/tables/official/csv/`; `CLAUDE.md` goes into the project's instructions. The operator receives these files copied flat into one folder: the zip in `download/`, built from this list by a script (see `download/`).
Never load: `fixtures/` · `expected/` · `rounds/` · `tools/` · `reference/pt/full/` · `reference/en/full/`. They exist to check the auditor; they are not part of it.

## How to check it
The evidence a reader uses to check the auditor lives in the folders on the never-load list: `fixtures/` (anonymised notes, one-field mutations, and one violation kept while the text around it is reworded three ways), `expected/` (what each fixture must return, committed before the run), `rounds/` (the office's recorded rounds, the author's fixture runs, two controls and the refusal, each with what it does not prove) and `tools/`. `tools/README.md` lists each claim this folder makes, the command that breaks it if it is false, and how to break it on purpose.

**Measured against the model alone** (`rounds/control-bare-model/`): given the same notes with no folder and web search on, the model alone covers more of the law than these checks do. Four things it never did, in any run: give a citation that can be checked offline; stop where a fact was missing; hand the decision back; return the same structure twice. Those four are what this folder is for, and the folder did them on Claude Opus 4.8 at low effort in every run. What each run proves and does not prove: `rounds/control-bare-model/what-this-shows.md`.

**Who the witness is.** A real accounting firm, in operation. It provides accounting services to the author: the relationship is commercial and predates this competition. There is no personal relationship with anyone there. The office is also a potential client of the product. The rounds run inside its working routine, on notes of its real clients, under the conditions in `rounds/CONSENT.md`; roles, never names (`rounds/README.md` § Roles).

**How it was built.** With Claude, in the open: the request for the first round is the first commit; predictions precede reports; nothing in a report was edited after the run. This README was rewritten and measured on 11/09/2026, after round 1: the whole file shrank by about 16% and the Portuguese step-by-step grew by about 9%, because seven vague instructions became seventeen commands (the numbers and the method are in `rounds/round-1-v1/what-changed.md`); the version the office received for round 1 is at commit `ac96786`, the version before the rewrite at `6035cb9`.
