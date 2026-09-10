# expected — fixture run in the v2 shape (written before the run, 10/09/2026, night)

**Why this run.** `rules.md` § 3 changed today (check cell with its label; severity with who acts; short location; CSV block at the end; Portuguese header `verificação`) and § 0 changed today (profile line of three fields copied from the sheet). No report in this shape exists yet; `examples.md` holds three tables in the earlier shape, kept verbatim under a dated note. The question this run answers: **reading the rules as they stand, with the old examples loaded, does the auditor return the new shape, or does it imitate the examples?** Round 2 with the Employee is tomorrow morning; if it imitates, the fix is tonight.

**What is fed.** `fixtures/mutations/m1-codigo-servico/nfse.xml` (cTribNac 171901 → 010101, one field changed) + the line
`perfil: Regime tributário = Simples Nacional - Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719`
(the office's own cells composed in the sheet's style, as declared in `expected/m1-codigo-servico.md`).

**Conditions.** claude.ai in the browser (the same project the author's runs used, `nfse-auditor`, Marcelo's account), Chat mode, no tools; project knowledge updated tonight with today's `rules.md`, `identity.md`, `README.md`, `examples.md`, `TABLES.md`; instructions = today's `CLAUDE.md`; model Claude Opus 4.8, effort low — the setting every fixture run used. Operator: the author's session, driving the browser. One message, one note.

**What must come back, in this order:**
1. `Totais para a sua comparação:` — 08/2026, R$ 400,00.
2. One table with the header `| nota | verificação | dispositivo | resultado | severidade | localização | trecho citado |` — eight rows; every `verificação` cell = id ` · ` label, the eight labels of § 3 verbatim; `1-código` FALHA with severity `corrigir antes de fechar · você decide antes de fechar`; every other severity `—`; `1-descrição` NÃO DÁ PARA DETERMINAR; 2, 3, 5-aritmética PASSA; 4 PASSA with the row saying how the regime cell was read (optant); 5-alíquota NÃO SE APLICA; 6 NÃO SE APLICA. Location cells short: the decisive field with its value and the other side of the comparison (for `1-código`: `cTribNac = 010101` (01.01) × cadastro `1719`), no field lists. Quotes verbatim from `reference/pt/excerpts/`.
3. `Não lidos:` none.
4. The line `Copie o bloco abaixo…` and a fenced `csv` block: header `nota;verificação;dispositivo;resultado;severidade;localização;trecho citado`, `;` separator, quoted cells, eight rows, `localização` full (the corroborating fields the table left out).

**Failure modes this run can show, and what each would mean:** (a) the old header `check` or bare check ids — the examples won, the rule lost: fix tonight (the note in `examples.md` is not enough; the examples' tables get a v2 twin or leave the loaded set); (b) no CSV block — the CLAUDE.md sentence and § 3 are not enough: fix tonight; (c) labels reworded — the closed vocabulary is not closed enough: fix tonight; (d) long location — § 3's "SHORT" not read: fix tonight; (e) the regime cell not read as optant — § 0's reading rule failed: fix tonight.

**What this run does not prove:** that the Employee reads the new table better (that is round 2); anything about the desktop app on Windows (this is the browser); anything about Opus 5 (not used).
