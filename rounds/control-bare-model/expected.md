# Control — the bare model, no folder at all — expected (written 2026-09-09 ~13:15, before the run)

**Why this run exists.** `control-no-reference/` measured the folder without its standard. This one measures **no folder**: a plain chat, no project, no entry file, no `identity.md`, no `rules.md`, no `reference/`. The same note and the same profile line, and one ordinary request. It answers the question a reader is entitled to ask: would any capable model do this on its own?

**Set-up (fixed, so a reader can repeat it).** A new conversation outside any project. Attach the XML, paste the profile line, and send exactly this request:

    Confira esta nota fiscal de serviço (NFS-e) contra as normas que se aplicam a ela: a lei do ISS, o Simples Nacional e o leiaute nacional da NFS-e. Diga o que passa e o que falha, onde, e cite a norma. A linha "perfil" é o cadastro do cliente.

Runs planned (the author decides how many are done; each is one conversation):
- **B1** `fixtures/clean/nfse-01.xml` + profile — Claude Opus 4.8, effort "low" (the model and effort of the folder runs, for a fair pair).
- **B2** `fixtures/mutations/m1-codigo-servico/nfse.xml` + profile — same model.
- **B3, B4** the same two on a stronger model and effort (Claude Fable 5.1, high), to see whether a stronger model closes the gap without the folder.

**Prediction.**
1. The bare model produces a review, probably a list or a table, with article numbers from memory. Some will be right (LC 116 art. 3, art. 7; LC 123 art. 13). The quoted text, when it quotes, will not be verbatim: C1 run on the transcript reports every quote as unresolved.
2. **On the clean note (B1/B3)** it will likely raise the rate as a problem — 2% on the note against 5% in Aracaju's table, or "check the rate" — instead of NOT APPLICABLE for a Simples optant paying fixed ISS (the folder's failure mode 4). It will likely not separate "cannot determine" from pass/fail: the description × code judgement will be decided one way or the other.
3. **On the wrong-code note (B2/B4)** it will likely catch the code (01.01 on an accounting client), because the profile line says 17.19 — that part is easy — and will likely tell the operator which code to use (the advice the folder refuses).
4. Neither run will report pass and fail per check in a fixed order, nor list what it could not check.
5. The stronger model (B3/B4) will be more accurate on the law and still not verbatim, and still likely to advise.

**How it is measured.** (a) `tools/check_audit.py` in control mode on the transcript: resolvable quotes (expected: none). (b) Row by row against `expected/nfse-01.md` and `expected/m1-codigo-servico.md`: results that match, false FAILs (the rate trap), judgements decided that the folder returns as CANNOT DETERMINE, and advice given. Written into `what-this-shows.md` after the run, from the checker's output and the comparison, never typed from memory.

**What this will not prove.** One or two notes, one run per model, low effort on one of them. It does not rank models; it shows what a plain request returns next to what the folder returns on the same input.

## Addendum — 2026-09-09 ~13:45, after B1 and before any further run

**Condition of B1, learned after it ran:** web search was **on** in that chat. The author's definition of the control (09/09): the model with everything it can do on its own, web included, without the folder. So B1 stands as the control; the runs below keep web on.

**Prediction 2 above was wrong for B1:** the bare model did not fall for the rate table; it recognised the IBPT figures as informational. It did advise (corrections written out), it did produce no checkable rows (the checker read 0), and its citations do not open in the folder (one verbatim, one reworded, two from sources not in the folder). It also raised `regEspTrib = 0` (a field the folder does not check) — a candidate check, and a question for the office.

**B2 and B4 dropped** (author, 09/09): catching code 01.01 on an accounting client whose profile says 17.19 is easy for any model, and the advice was already shown in B1.

**B5 — the null case, bare:** Claude Opus 4.8, effort "low", web on; `fixtures/clean/nfse-02.xml` attached, **no profile line**, the same fixed request. The folder returned CANNOT DETERMINE on `1-código`, `1-descrição`, `4`, `5-alíquota` (example 4b). Prediction: the bare model reads the regime and the item from the note's own flags and free text (`opSimpNac = 3`, "Fixo Contador") and gives verdicts on them — it does not say "cannot determine without the client's registration". If it does say so, the folder's second claim is weaker than we think, and that goes in `what-this-shows.md` too.

**B3 — the ceiling:** Claude Fable 5.1, effort "high", web on; `fixtures/clean/nfse-01.xml` + profile line. Prediction: more accurate on the law than B1, still no verbatim quotes the checker can resolve, still advises.
