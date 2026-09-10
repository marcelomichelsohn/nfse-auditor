# what-changed — fixture run in the v2 shape (10/09/2026, night), against the prediction

**The question the run answered:** reading `rules.md` as it stands, with the three old-shape examples loaded under a dated note, does the auditor return the new shape or imitate the examples? **It returned the new shape.** Every element the prediction named came: the totals line; the header `verificação`; the eight labels of § 3 verbatim in every `verificação` cell; `1-código` FALHA with `corrigir antes de fechar · você decide antes de fechar`; every other severity `—`; the results row by row as predicted (1-descrição NÃO DÁ PARA DETERMINAR; 2, 3, 4, 5-aritmética PASSA; 5-alíquota and 6 NÃO SE APLICA); the short location with the two sides of each comparison (`cTribNac = 010101` × `Código de Atividade = 1719`; `xDescServ` × the code's official description); verbatim quotes; `Não lidos`; the line before the CSV word for word; the CSV block with `;`, quoted cells, doubled inner quotes, the full location in its `localização` cell. None of the five failure modes listed in `expected.md` appeared. `python3 tools/check_audit.py` reads this folder's `report.md` and passes.

**Divergences from the prediction, small, kept as they came:**
1. The answer opened with one English sentence before the report (`I'll work through this note against the checks.`). Not part of the report; § 3 says the report starts at the totals line. Noted, not fixed tonight.
2. The `1-código` location says `× perfil` where § 3's example says `× cadastro`; the `4` location says `perfil Regime = Simples Nacional` and the reading ("lido como optante") appears only in the CSV's full location, not in the table's short one. Same content, the word the operator reads differs from the rule's example. Noted.
3. The item comparison used the first four digits of `cTribNac` against the sheet's four-digit cell, as § 0 says — and worked on the first try.

**Conditions that differ from the product's route, declared:** the XML was pasted as text, not attached (the browser session was not allowed to attach a file to the message; the `nota` column took the file name given in the text); the web app fetched the project's files with tools ("Read 4 files, ran 6 commands"), where the desktop app's earlier runs showed no tool steps; Opus 4.8 at low effort, the fixture setting, not the model the office's account shows.

**What this run does not prove:** that the Employee reads the new table better (round 2, tomorrow morning); anything about the desktop app on Windows; anything about Opus 5.

**Changes to the folder because of this run:** none tonight. Example 5 in `examples.md` is this report, so the loaded set now carries one table in the current shape beside the three earlier ones.
