# Timing control, v1 × v2 — expected (written 11/09/2026, after round 2 ran and before any run of this control; committed before the first run)

**The question.** Do the v2 instructions make the model's audit shorter than the v1 instructions, with everything else held equal? Round 1 and round 2 cannot answer it: between them four things changed (instructions, route, model, effort), and both ran on the office's account and machine. This control changes one thing.

**Design — what is held equal, per run, declared here so the record cannot drift.**
- **Model and effort:** Claude Opus 4.8, effort low, in every run.
- **Route:** a Claude project on the author's account (claude.ai in Chrome), Chat mode, the version's files uploaded to the project's knowledge and its `CLAUDE.md` pasted into the instructions; one new conversation per run.
- **Input:** the same file and the same facts in every run of the same note. The XML is attached if the chat allows it that day, or pasted as text if attaching is blocked (as it was on 10/09); whichever it is, it is the same for v1 and v2 and is written in the transcript. The profile line carries the same facts in both versions but in each version's own form, because the form is part of the instructions under test: v1 `perfil: CNAE 6920-6/01; regime Simples optante; anexo III; município 2800308; item LC 116 17.19; exporta não`; v2 `Regime tributário = Simples Nacional - Comércio e ou Serviço - Com Pró-labore - Com Funcionários; Anexo = III; Código de Atividade = 1719`.
- **v1:** the repository as the Employee received it for round 1, commit `ac96786` — its loaded files built by that commit's own `tools/make_load_folder.py` (`git archive ac96786 | tar -x -C <dir>; python3 <dir>/tools/make_load_folder.py <out>`), uploaded to a fresh project. **v2:** the repository at the commit that carries this file, built by the same script.
- **v1 is re-run fresh.** The time of round 1 never enters as the v1 side (round 1 ran on Opus 5 at high effort, through Cowork, with tools reading the disk, on the office's machine); the time of round 2 never enters as the v2 side (the office's account and machine). Neither is comparable to a run here.
- **Two notes, two runs each per version — eight runs.** (i) The public fixture `fixtures/mutations/m1-codigo-servico/nfse.xml` (wrong service code; runs and reports published in full). (ii) The client's note of rounds 1 and 2 (wrong service code, 31.01 against the sheet's 7.02), run outside this repository: only its numbers enter (time, tool calls, files read, answer length); nothing of the note, as `round-1-v1/expected.md` promised. The fixture pair runs first; the real-note pair after round 2's transcript is processed.

**What is measured, per run, and how.**
- Time from send to the end of the answer, by a stopwatch started at the click, to the second (the interface shows no run time in Chat).
- Tool calls and files read, as the interface reports them ("Read N files, ran M commands"), and the file names where the expanded steps show them.
- Length of the answer in characters (`wc -m` on the saved answer).
- Whether the report has the version's shape and the expected rows (v1: `examples.md` at `ac96786`, example 1; v2: `fixture-runs-v2/expected.md`), checked by `tools/check_audit.py` for the fixture runs.

**What we expect, written first.**
1. On the fixture: the v2 runs take **no longer** than the v1 runs and read **no more files**; we do not predict that v2 is faster, because v2's `rules.md` § 3 is longer than v1's (the label vocabulary, the severity classes, the CSV block) and the answer is longer by the CSV block, which costs output time. The honest prediction is "v2 costs about the same; the CSV block is the visible extra".
2. "v2 is faster" is claimed only if both v2 runs are shorter than both v1 runs on the same note, and read no more files. "v2 is slower" is written if both v2 runs are longer than both v1 runs. Anything else is "no difference the two runs can see".
3. Tool calls: fewer in v2 than v1 if the model reads only what `rules.md` § 1 names; more if the longer § 3 sends it back to the file. We do not predict which.
4. On the real note: the same shape of result as on the fixture; the check-1 FAIL on both versions.

**What this control will not prove.** Two runs per cell, one operator (the author), the author's account, one day; a stopwatch and the interface's own counters, not the office's clock; the XML pasted as text if attaching is blocked, which the office's route does not do. It does not measure the Employee's time; it measures the model's work under each set of instructions.

**Order.** This file committed and pushed before the first run; `transcript.md` (the eight runs, times, counters, the fixture answers in full, the real note's numbers only) after; `what-this-shows.md` last.
