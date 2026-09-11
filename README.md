# nfse-auditor

As instruções de uso vêm duas vezes: primeiro em português, para quem vai usar a pasta no escritório; depois em inglês. As duas dizem a mesma coisa; o resto do arquivo está só em inglês.

The instructions come twice: first in Portuguese, for the person who will use the folder at the accounting office in Brazil; then in English. The two say the same thing; the rest of this file is in English only.

## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação, ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Descompacte o arquivo que você recebeu.
2. No app do Claude, no menu da esquerda, clique em "Projetos" e crie um projeto novo com o nome `nfse-auditor` (se já existir um com esse nome, use outro nome). Deixe o campo "Pasta" vazio.
3. Abra o arquivo `CLAUDE.md` da pasta descompactada (se o computador perguntar com que programa abrir, escolha o Bloco de Notas). Selecione tudo e copie.
4. No projeto, no painel da direita, em "Instruções", cole o que copiou e salve.
5. No mesmo painel, em "Contexto", adicione todos os outros arquivos da pasta descompactada, selecionando todos de uma vez.

**Como usar:**

6. Dentro do projeto, comece uma conversa nova. Na caixa de mensagem, deixe marcado "Chat", não "Cowork".
7. Ao lado da caixa de mensagem, onde aparece o nome do modelo, escolha "Opus 4.8" (abra a lista completa de modelos se ele não estiver à vista) e o esforço "Baixo".
8. Anexe um arquivo XML de nota fiscal do padrão nacional. Uma nota por conversa.
9. Na mesma mensagem, escreva uma linha com três células da sua planilha de controle, da linha desse cliente, cada uma depois do nome da coluna, copiadas do jeito que estão escritas: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (exemplo). Se a célula tiver mais de um valor, copie a célula inteira.
10. Envie. Você recebe de volta uma linha de totais, uma tabela (nota · verificação · dispositivo · resultado · severidade · localização · trecho citado), a lista "Não lidos" e, por último, as mesmas linhas num bloco CSV, com a localização completa, para você copiar e colar numa planilha (não é um arquivo pronto: é texto que você copia). Nada mais. Leva alguns minutos por nota.

Os nomes entre aspas são os da tela do app em português, vistos em 09/09/2026; versões novas do app podem mudá-los.

**Três situações em que ela para em vez de adivinhar:** sem a linha do passo 9, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo) entra em "Não lidos"; um pedido de decisão ("qual item eu uso?") volta para você, com a nota e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**What it is.** A folder that audits Brazilian service invoices (NFS-e, national standard) under the ISS law, the Simples Nacional and the national layout. For each note and each check it returns pass / fail / cannot determine / not applicable, with the provision quoted verbatim. It corrects nothing and decides nothing for you.

**Set-up, once:**

1. Unpack the file you received.
2. In the Claude app, open the projects list and create a new project named `nfse-auditor` (if one with that name already exists, use another name). Leave the project's folder field empty.
3. Open the unpacked folder's `CLAUDE.md` (a plain-text editor will do). Select all and copy.
4. In the project, paste what you copied into the project's own instructions field (not a conversation) and save.
5. In the same panel, under the project's context, add every other file of the unpacked folder, selecting them all at once.

**Use:**

6. Inside the project, start a new conversation. In the message box, keep "Chat" selected, not "Cowork".
7. Beside the message box, where the model's name shows, choose "Opus 4.8" (open the full list of models if it is not in view) and the effort "Low".
8. Attach one national-standard NFS-e XML file. One note per conversation.
9. In the same message, write one line with three cells of the office's control spreadsheet, from that client's row, each after its column name, copied as written: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702` (an example). If a cell holds more than one value, copy the whole cell.
10. Send. You get back a totals line, a table (note · check · provision · result · severity · location · quoted excerpt), the "Not read" list and, last, the same rows as a CSV block, with the full location, for you to copy into a spreadsheet (not a ready-made file: text you copy). Nothing else. It takes a few minutes per note.

The names in quotes are the labels of the app's Portuguese screen, seen on 09/09/2026; the English steps name each field by what it does, because no one has checked the English screen.

**Three situations where it stops instead of guessing:** without the line of step 9, the checks that need it return "cannot determine"; a file that is not national-standard XML (a municipality's own, for instance) goes under "Not read"; a request for a decision ("which item should I use?") is handed back, with the note and the rule beside it.

**What it does not do:** it does not fetch notes, compute the monthly tax (DAS), compare the client's declared revenue with the notes (it only sums the notes for you to compare), read a municipality's own XML or a PDF, validate the digital signature, or decide anything for you.

## What to load, and what never to load
What to load: the files the operator's folder contains, and nothing else. `identity.md` · `rules.md` · `examples.md` · `README.md` · `reference/INDEX.md` · `reference/pt/excerpts/` · `reference/en/excerpts/` · `reference/tables/required-fields.md` · `reference/tables/TABLES.md` · `reference/tables/working/` · `reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` · `reference/tables/official/csv/`; `CLAUDE.md` goes into the project's instructions. The operator receives these files copied flat into one folder, which is why the steps speak of one folder and no subfolders.
Never load: `fixtures/` · `expected/` · `rounds/` · `tools/` · `reference/pt/full/` · `reference/en/full/`. They exist to check the auditor; they are not part of it.

## How to check it
The evidence a reader uses to check the auditor lives in the folders on the never-load list: `fixtures/` (anonymised notes, one-field mutations, and one violation kept while the text around it is reworded three ways), `expected/` (what each fixture must return, committed before the run), `rounds/` (the office's recorded rounds, the author's fixture runs, two controls and the refusal, each with what it does not prove) and `tools/`. `tools/README.md` lists each claim this folder makes, the command that breaks it if it is false, and how to break it on purpose.

**Measured against the model alone** (`rounds/control-bare-model/`): given the same notes with no folder and web search on, the model alone covers more of the law than these checks do. Four things it never did, in any run: give a citation that can be checked offline; stop where a fact was missing; hand the decision back; return the same structure twice. Those four are what this folder is for, and the folder did them on Claude Opus 4.8 at low effort in every run. What each run proves and does not prove: `rounds/control-bare-model/what-this-shows.md`.

**How it was built.** With Claude, in the open: the request for the first round is the first commit; predictions precede reports; nothing in a report was edited after the run. This README was rewritten and cut on 11/09/2026, after round 1 (the measurement is in `rounds/round-1-v1/what-changed.md`); the version the office received for round 1 is at commit `ac96786`, the version before the cut at `6035cb9`.
