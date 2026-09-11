# nfse-auditor

This README is written in two languages: first in Portuguese, for the person who will use the folder at the accounting office in Brazil; then in English, for everyone else, the judges included. The two say the same thing.

## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação (cada linha da tabela), ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Descompacte o arquivo que você recebeu. Todos os arquivos ficam soltos dentro da pasta, sem subpastas.
2. No app do Claude, crie um Projeto novo com o nome `nfse-auditor`. O app tem dois modos de conversa, Chat e Cowork; esta pasta foi testada no Chat, com os arquivos subidos ao Projeto. Se o app oferecer "Adicionar pasta" ou pedir acesso ao seu disco, esse é o outro caminho: não use.
3. No painel do Projeto, clique no lápis "Edit instructions" (editar instruções). Abra o arquivo `CLAUDE.md` da pasta (na lista de arquivos ele pode aparecer só como `CLAUDE`; se o computador perguntar com que programa abrir, escolha o Bloco de Notas), selecione tudo, copie, cole na caixa "Set project instructions" e clique em "Save instructions" (salvar).
4. No mesmo painel, em "Context" (contexto), clique em "+" e depois em "Add files" (adicionar arquivos). Selecione todos os outros arquivos da pasta de uma vez e confirme; a lista mostra cada arquivo que subiu. Não precisa ler nenhum deles.

**Como usar:**

5. Abra uma conversa nova dentro do Projeto e confira que o botão do compositor está em "Chat", não em "Cowork". No seletor de modelo, abra "More models" (mais modelos) e escolha **Opus 4.8**; em "Effort" (esforço), escolha **Low** (baixo). Foi com esse modelo e esse esforço que a pasta foi testada. Anexe um arquivo XML do emissor nacional, e só um: para a nota seguinte, abra outra conversa.
6. Na mesma mensagem, escreva uma linha com três células da sua planilha de controle, as da linha desse cliente, cada uma depois do nome da coluna, neste formato: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702`. Isso é só um exemplo: copie o que está na sua planilha, do jeito que está escrito, sem traduzir. Se a célula tiver mais de um valor, copie a célula inteira (por exemplo `Anexo = III - V` ou `Código de Atividade = 1008 / 106 / 2301`).
7. Envie. Volta uma linha de totais, uma tabela (nota · verificação · dispositivo · resultado · severidade · localização · trecho citado), a lista "Não lidos" e, por último, as mesmas linhas num bloco CSV, com a localização completa, para você copiar e colar numa planilha (não é um arquivo pronto: é texto que você copia). Nada mais. Leva alguns minutos por nota.

Os nomes dos botões acima foram conferidos no app do Claude aberto no navegador (claude.ai), em 10/09/2026, numa conta em inglês. No aplicativo instalado no Windows, ou numa conta em português, eles podem aparecer com outro nome ou em outro lugar.

**Três situações em que ela para em vez de adivinhar:** sem a linha do passo 6, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo, que começa com `<CompNfse>`) entra em "Não lidos" e não é conferido; um pedido de decisão ("qual item eu uso?") volta para você, com a nota, a linha do passo 6 e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**What it is.** A folder that audits Brazilian service invoices (NFS-e, national standard) under the ISS law, the Simples Nacional and the national layout. For each note and each check it returns pass / fail / cannot determine / not applicable, with the provision quoted verbatim. It corrects nothing and decides nothing for you.

**Set-up, once:**

1. Unpack the file you received. Every file sits loose inside the folder, no subfolders.
2. In the Claude app, create a new project named `nfse-auditor`. The app has two conversation modes, Chat and Cowork; this folder was tested in Chat, with the files uploaded to the project. If the app offers "Add folder" or asks for access to your disk, that is the other path: do not take it.
3. In the project's panel, click the pencil "Edit instructions". Open the folder's `CLAUDE.md` (the file list may show it as just `CLAUDE`; a plain-text editor will do), select all, copy, paste into the "Set project instructions" box and click "Save instructions".
4. In the same panel, under "Context", click "+" and then "Add files". Select every other file of the folder at once and confirm; the list shows each file that went up. There is no need to read any of them.

**Use:**

5. Open a new conversation inside the project and check that the composer's switch is on "Chat", not "Cowork". In the model selector, open "More models" and choose **Opus 4.8**; under "Effort", choose **Low**. That is the model and the effort the folder was tested on. Attach one national-standard XML file, and only one: for the next note, open another conversation.
6. In the same message, write one line with three cells of the office's control spreadsheet, from that client's row, each after its column name, in this form: `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 702`. That is only an example: copy what the sheet says, as written, without translating. If a cell holds more than one value, copy the whole cell (for instance `Anexo = III - V` or `Código de Atividade = 1008 / 106 / 2301`).
7. Send. You get back a totals line, a table (note · check · provision · result · severity · location · quoted excerpt), the "Not read" list and, last, the same rows as a CSV block, with the full location, for you to copy into a spreadsheet (not a ready-made file: text you copy). Nothing else. It takes a few minutes per note.

The button names above were checked in the Claude app in the browser (claude.ai) on 10/09/2026, on an account in English. In the app installed on Windows, or on an account in Portuguese, they may carry another name or sit elsewhere.

**Three situations where it stops instead of guessing:** without the line of step 6, the checks that need it return "cannot determine"; a file that is not national-standard XML (a municipality's own, for instance, starting with `<CompNfse>`) goes under "Not read" and is not audited; a request for a decision ("which item should I use?") is handed back, with the note, the line of step 6 and the rule beside it.

**What it does not do:** it does not fetch notes, compute the monthly tax (DAS), compare the client's declared revenue with the notes (it only sums the notes for you to compare), read a municipality's own XML or a PDF, validate the digital signature, or decide anything for you.

## What to load, and what never to load
What to load: the files the operator's folder contains, and nothing else. `identity.md` · `rules.md` · `examples.md` · `README.md` · `reference/INDEX.md` · `reference/pt/excerpts/` · `reference/en/excerpts/` · `reference/tables/required-fields.md` · `reference/tables/TABLES.md` · `reference/tables/working/` · `reference/tables/municipal-rates_2800308-aracaju-se_extract-20260903.csv` · `reference/tables/official/csv/`; `CLAUDE.md` goes into the project's instructions.
Never load: `fixtures/` · `expected/` · `rounds/` · `tools/` · `reference/pt/full/` · `reference/en/full/`. They exist to check the auditor; they are not part of it.

`tools/make_load_folder.py` builds the operator's folder from this repository: the files above, flattened (a Claude project ignores subfolders, and every file name here is unique), zipped for sending, with this README also rendered as HTML so it can be opened on any computer. The repository keeps its structure because that is where a reader checks the auditor; the flat folder is only how it is delivered.

## The auditor and its evidence are different folders
Everything a reader uses to check the auditor lives beside it, in the folders the list above says never to load: `fixtures/` (anonymised notes and one-field mutations), `expected/` (what each fixture must return, written before the run), `rounds/` (the office's recorded rounds, the author's fixture runs, two controls and the refusal — the auditor asked three ways to decide for the operator, and handing it back — each with what it does not prove), `tools/`, and the full texts of the standard under `reference/`. `check_audit.py` checks, offline and in one command, that every quote in every report appears word for word in a file under `reference/`; `prove_order.py` reads from git the order of the predictions and the reports. The Portuguese text is the one that counts; the English beside it exists so a reader who does not read Portuguese can follow a citation.

## What the folder adds, measured against the model alone
The same notes were also given to the model with no folder at all and web search on (`rounds/control-bare-model/`). The model alone covers more of the law than the checks here do, and it found real defects these checks do not look for; some of them are now candidate checks. Four things it did not do in any run. It never gave the reader a citation that can be checked offline: its citations point to sources the reader has to go and find, and none of them can be checked against a fixed file — the checker read no table row at all. It never stopped where a fact was missing: given no client profile, it took the regime from the note's own free text and rewrote the note. It never handed the decision back: it prescribed corrections every time. And it never returned the same structure for every note. Those four things are what this folder is for. It is not a model that knows ISS; it is the layer that makes a capable model's audit checkable by a stranger and repeatable by an accounting firm. It did that on Claude Opus 4.8 at low effort in every run; the model alone covered more ground only on Claude Fable 5.1 at high effort with the web, and was still not checkable. For an office that closes the books for dozens of clients a month, that is what decides whether the folder can run on every note. A smaller model with the folder, and the cost per report, were not measured. What each run proves and does not prove is in `rounds/control-bare-model/what-this-shows.md`.

## The rounds
`rounds/README.md` is the index: round 0 (the office's assistant closing a month by hand, recorded 08/09/2026), the author's fixture runs and what each changed (`rounds/fixture-runs-v1/what-changed.md`), the control without `reference/`, the control without the folder at all, and the refusal.
What round 0 showed. The recording shows the office's assistant closing a month at the level of totals and codes, across three systems and a spreadsheet, without opening an individual note. The office owner, on 09/09/2026, added the figures: the analysis of a client averages about twenty minutes when nothing is wrong and can take hours when something is (one client took five); today's issuing errors are few, because issuing is still simple, and she expects them to grow with the tax reform's new codes; one client issued a note with the wrong service code last month; ISS is withheld for one client only. So the per-note check this folder performs is not the office's step today: it is the step the reform makes necessary, and the office's larger pain — a note that does not reach the national portal at closing time — is recorded as the next version. Whether any client is already checked note by note is the one question still with the assistant.
What the fixture runs and the controls do not prove: the author ran them himself, on notes of his own company; a person from the office using the folder is what the next rounds are for.

## How it was built
With Claude, in the open: the request for the first round is the first commit; predictions precede reports; nothing in a report was edited after the run. This README is the version the office's assistant received for round 1; earlier versions are in git.
