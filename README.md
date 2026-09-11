# nfse-auditor

As instruções de uso vêm duas vezes: primeiro em português, para quem vai usar a pasta no escritório; depois em inglês. As duas dizem a mesma coisa; o resto do arquivo está só em inglês.

The instructions come twice: first in Portuguese, for the person who will use the folder at the accounting office in Brazil; then in English. The two say the same thing; the rest of this file is in English only.

## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação, ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Descompacte o arquivo que você recebeu. Todos os arquivos ficam soltos dentro da pasta, sem subpastas.
2. No app do Claude, crie um Projeto novo com o nome `nfse-auditor`. O app tem dois modos de conversa, Chat e Cowork; esta pasta foi testada no Chat, com os arquivos subidos ao Projeto. Se o app oferecer adicionar uma pasta inteira, ou pedir acesso ao seu disco, não aceite: esta pasta não foi testada assim.
3. No painel do Projeto, clique no lápis "Edit instructions" (editar instruções). Abra o arquivo `CLAUDE.md` da pasta (na lista de arquivos ele pode aparecer só como `CLAUDE`; se o computador perguntar com que programa abrir, escolha o Bloco de Notas), selecione tudo, copie, cole na caixa "Set project instructions" e clique em "Save instructions" (salvar).
4. No mesmo painel, em "Context" (contexto), clique em "+" e depois em "Add files" (adicionar arquivos). Selecione todos os outros arquivos da pasta de uma vez e confirme; a lista mostra todos os arquivos que entraram. Não precisa ler nenhum deles.

**Como usar:**

5. Abra uma conversa nova dentro do Projeto e confira que a conversa está em "Chat", não em "Cowork". No seletor de modelo, abra "More models" (mais modelos) e escolha **Opus 4.8**; em "Effort" (esforço), escolha **Low** (baixo). Foi com esse modelo e esse esforço que a pasta foi testada. Anexe um arquivo XML do padrão nacional, e só um: para a nota seguinte, abra outra conversa.
6. Na mesma mensagem, copie três células da sua planilha de controle, da linha desse cliente. Escreva o nome da coluna, o sinal de igual e o valor, neste formato: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702`. Isso é só um exemplo: copie o que está na sua planilha, do jeito que está escrito, sem traduzir. Se a célula tiver mais de um valor, copie a célula inteira (por exemplo `Anexo = III - V` ou `Código de Atividade = 1008 / 106 / 2301`).
7. Envie. Você recebe de volta uma linha de totais, uma tabela (nota · verificação · dispositivo · resultado · severidade · localização · trecho citado), a lista "Não lidos" e, por último, as mesmas linhas num bloco CSV, com a localização completa, para você copiar e colar numa planilha (não é um arquivo pronto: é texto que você copia). Nada mais. Leva alguns minutos por nota.

Os nomes dos botões acima foram conferidos no app do Claude aberto no navegador (claude.ai), em 10/09/2026, numa conta em inglês. No aplicativo instalado no Windows, ou numa conta em português, eles podem aparecer com outro nome ou em outro lugar.

**Três situações em que ela para em vez de adivinhar:** sem a linha do passo 6, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo) entra em "Não lidos"; um pedido de decisão ("qual item eu uso?") volta para você, com a nota e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**What it is.** A folder that audits Brazilian service invoices (NFS-e, national standard) under the ISS law, the Simples Nacional and the national layout. For each note and each check it returns pass / fail / cannot determine / not applicable, with the provision quoted verbatim. It corrects nothing and decides nothing for you.

**Set-up, once:**

1. Unpack the file you received. Every file sits loose inside the folder, no subfolders.
2. In the Claude app, create a new project named `nfse-auditor`. The app has two conversation modes, Chat and Cowork; this folder was tested in Chat, with the files uploaded to the project. If the app offers to add a whole folder, or asks for access to your disk, do not accept: this folder was not tested that way.
3. In the project's panel, click the pencil "Edit instructions". Open the folder's `CLAUDE.md` (the file list may show it as just `CLAUDE`; a plain-text editor will do), select all, copy, paste into the "Set project instructions" box and click "Save instructions".
4. In the same panel, under "Context", click "+" and then "Add files". Select every other file of the folder at once and confirm; the list shows every file that was uploaded. There is no need to read any of them.

**Use:**

5. Open a new conversation inside the project and check that the conversation is on "Chat", not "Cowork". In the model selector, open "More models" and choose **Opus 4.8**; under "Effort", choose **Low**. That is the model and the effort the folder was tested on. Attach one national-standard XML file, and only one: for the next note, open another conversation.
6. In the same message, copy three cells of the office's control spreadsheet, from that client's row. Write the column name, an equals sign and the value, in this form: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702`. That is only an example: copy what the sheet says, as written, without translating. If a cell holds more than one value, copy the whole cell (for instance `Anexo = III - V` or `Código de Atividade = 1008 / 106 / 2301`).
7. Send. You get back a totals line, a table (note · check · provision · result · severity · location · quoted excerpt), the "Not read" list and, last, the same rows as a CSV block, with the full location, for you to copy into a spreadsheet (not a ready-made file: text you copy). Nothing else. It takes a few minutes per note.

The button names above were checked in the Claude app in the browser (claude.ai) on 10/09/2026, on an account in English. In the app installed on Windows, or on an account in Portuguese, they may have a different name or be somewhere else.

**Three situations where it stops instead of guessing:** without the line of step 6, the checks that need it return "cannot determine"; a file that is not national-standard XML (a municipality's own, for instance) goes under "Not read"; a request for a decision ("which item should I use?") is handed back, with the note and the rule beside it.

**What it does not do:** it does not fetch notes, compute the monthly tax (DAS), compare the client's declared revenue with the notes (it only sums the notes for you to compare), read a municipality's own XML or a PDF, validate the digital signature, or decide anything for you.

## What to load, and what never to load
What to load: the files the operator's folder contains, and nothing else. `identity.md` · `rules.md` · `examples.md` · `README.md` · `reference/INDEX.md` · `reference/pt/excerpts/` · `reference/en/excerpts/` · `reference/tables/required-fields.md` · `reference/tables/TABLES.md` · `reference/tables/working/` · `reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` · `reference/tables/official/csv/`; `CLAUDE.md` goes into the project's instructions. The operator receives these files copied flat into one folder, which is why step 1 says no subfolders.
Never load: `fixtures/` · `expected/` · `rounds/` · `tools/` · `reference/pt/full/` · `reference/en/full/`. They exist to check the auditor; they are not part of it.

## How to check it
The evidence a reader uses to check the auditor lives in the folders on the never-load list: `fixtures/` (anonymised notes, one-field mutations, and one violation kept while the text around it is reworded three ways), `expected/` (what each fixture must return, committed before the run), `rounds/` (the office's recorded rounds, the author's fixture runs, two controls and the refusal, each with what it does not prove) and `tools/`. `tools/README.md` lists each claim this folder makes, the command that breaks it if it is false, and how to break it on purpose.

**Measured against the model alone** (`rounds/control-bare-model/`): given the same notes with no folder and web search on, the model alone covers more of the law than these checks do. Four things it never did, in any run: give a citation that can be checked offline; stop where a fact was missing; hand the decision back; return the same structure twice. Those four are what this folder is for, and the folder did them on Claude Opus 4.8 at low effort in every run. What each run proves and does not prove: `rounds/control-bare-model/what-this-shows.md`.

**How it was built.** With Claude, in the open: the request for the first round is the first commit; predictions precede reports; nothing in a report was edited after the run. This README was rewritten and cut on 11/09/2026, after round 1 (the measurement is in `rounds/round-1-v1/what-changed.md`); the version the office received for round 1 is at commit `ac96786`, the version before the cut at `6035cb9`.
