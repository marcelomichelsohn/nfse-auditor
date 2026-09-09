# nfse-auditor

This README is written in two languages: first in Portuguese, for the person who will use the folder at the accounting office in Brazil; then in English, for everyone else, the judges included. The two say the same thing.

## Para usar (português)

**O que é.** Uma pasta que confere notas fiscais de serviço (NFS-e) do padrão nacional contra a lei do ISS, o Simples Nacional e o leiaute nacional. Para cada nota e cada verificação (cada "check" da tabela), ela devolve passa / falha / não dá para determinar / não se aplica, com o trecho da norma citado ao pé da letra. Ela não corrige nada e não decide nada por você.

**Como montar, uma vez só:**

1. Descompacte o arquivo que você recebeu. Todos os arquivos ficam soltos dentro da pasta, sem subpastas.
2. No app do Claude, crie um Projeto novo. Dê o nome `nfse-auditor`.
3. Nas instruções do Projeto (o campo de texto do próprio Projeto, não uma conversa), cole o conteúdo do arquivo `CLAUDE.md`: abra o arquivo (se o computador perguntar com que programa abrir, escolha o Bloco de Notas), selecione tudo, copie e cole ali.
4. Adicione ao Projeto todos os outros arquivos da pasta, selecionando todos de uma vez. Não precisa ler nenhum deles.

**Como usar:**

5. Abra uma conversa nova dentro do Projeto e escolha o modelo Opus com esforço alto (High). Anexe um arquivo XML do emissor nacional: uma nota por conversa, que é como o sistema foi testado.
6. Na mesma mensagem, escreva uma linha com o perfil do cliente dessa nota, copiada da sua planilha de controle, neste formato: `perfil: CNAE 6920-6/01; regime Simples optante; anexo III; município 2800308; item LC 116 17.19; exporta não`. CNAE e item da lista de serviços como estão no cadastro; regime: Simples optante, MEI ou não optante; anexo: I a V, ou "fixo"; município: o código IBGE; exporta: sim ou não.
7. Envie. Volta uma linha de totais, uma tabela (nota · check · dispositivo · resultado · severidade · localização · trecho citado) e a lista "Não lidos". Nada mais. Leva alguns minutos por nota.

**Três situações em que ela para em vez de adivinhar:** sem a linha de perfil, as verificações que dependem dela voltam "não dá para determinar"; um arquivo que não é XML do padrão nacional (o da prefeitura, por exemplo, que começa com `<CompNfse>`) entra em "Não lidos" e não é conferido; um pedido de decisão ("qual item eu uso?") volta para você, com a nota, o perfil e a regra ao lado.

**O que ela não faz:** não baixa notas, não calcula o DAS, não compara o faturamento declarado com as notas (só soma as notas para você comparar), não lê o XML da prefeitura nem PDF, não valida assinatura digital, não decide nada por você.

## To use it (English)

**What it is.** A folder that audits Brazilian service invoices (NFS-e, national standard) under the ISS law, the Simples Nacional and the national layout. For each note and each check it returns pass / fail / cannot determine / not applicable, with the provision quoted verbatim. It corrects nothing and decides nothing for you.

**Set-up, once:**

1. Unpack the file you received. Every file sits loose inside the folder, no subfolders.
2. In the Claude app, create a new project. Name it `nfse-auditor`.
3. In the project's instructions (the project's own text field, not a conversation), paste the content of `CLAUDE.md`: open the file (a plain-text editor will do), select all, copy, paste.
4. Add every other file of the folder to the project, selecting them all at once. There is no need to read any of them.

**Use:**

5. Open a new conversation inside the project and choose the Opus model with high effort. Attach one national-standard XML file: one note per conversation, which is how the folder was tested.
6. In the same message, write one line with the profile of that note's client, copied from the office's control spreadsheet, in this form: `perfil: CNAE 6920-6/01; regime Simples optante; anexo III; município 2800308; item LC 116 17.19; exporta não`. CNAE and service-list item as registered; regime: Simples optante, MEI or não optante; annex: I to V, or "fixo" (fixed-amount ISS); municipality: the IBGE code; exporta: sim or não.
7. Send. You get back a totals line, a table (note · check · provision · result · severity · location · quoted excerpt) and the "Not read" list. Nothing else. It takes a few minutes per note.

**Three situations where it stops instead of guessing:** without the profile line, the checks that need it return "cannot determine"; a file that is not national-standard XML (a municipality's own, for instance, starting with `<CompNfse>`) goes under "Not read" and is not audited; a request for a decision ("which item should I use?") is handed back, with the note, the profile and the rule beside it.

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
