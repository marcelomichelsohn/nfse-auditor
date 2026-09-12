# Bare model — what each run shows, and what it does not (written 2026-09-09 after B1, B5 and B3; rewritten the same afternoon, one section per run, at the author's request)

**The question.** Without the folder — the model with everything it can do on its own, web search included — what does a plain request return, next to what the folder returns on the same input? Predictions and the condition (web on) are in `expected.md`. The measurements below come from `tools/check_audit.py` (control mode) and from a whitespace-normalised substring test of quoted sentences against `reference/pt/`.

---

## B1 — Claude Opus 4.8, effort "low", web on · clean note + profile line (`transcript-B1.md`)

**What came back.** A prose review, ordered "what fails / what passes / what must be verified", each item with risk and confidence. Incidence, service code, Simples flags, retention and values judged right. It did **not** fall for the municipal rate table: it read the IBPT figures as informational (prediction 2 of `expected.md` was wrong). It flagged `regApTribSN = 1` against the profile's fixed ISS as a **failure**, with the correction written out (`regApTribSN → 2`), and `regEspTrib = 0` where a society of professionals would carry 6 — a field the folder does not check. It ended with a section on what it could not confirm (whether Aracaju grants the fixed ISS to this office).

**What it proves.** A capable model with the web reads this note competently and knows more of the applicable law than the folder's six checks. It can spot a real inconsistency the folder only returns as CANNOT DETERMINE, and one the folder does not look at.

**What it does not prove.** That the review is checkable: the checker found **no report rows** (nothing to open against a provision); of four quoted sentences tested, one is verbatim in the folder's standard (§22-A), one is the layout rule reworded ("deixa de apurar… atribui" for "deixará de apurar… atribuir"), two come from web sources a reader of this repository cannot open. That it refrains from deciding: it prescribed the correction. That another run would say the same: one run.

---

## B5 — Claude Opus 4.8, effort "low", web on · clean note, **no profile line** (`transcript-B5.md`)

**What came back.** With no client registration given, the model took "Fixo Contador" from the note's free text as the client's regime, built two scenarios on it, and **rewrote the note**: an XML `regTrib` block to paste, a new `xOutInf` text, and an offer to fill in the municipal fixed amount and recompute `vISSQN` and `vLiq` once told the figure. It refused one thing: to invent the municipal amount.

**What it proves.** Without an instruction not to, the model fills a missing fact from whatever the note says about itself and acts on it. The folder, on the same input, returned CANNOT DETERMINE on the four checks that need the registration (`examples.md`, example 4b — after a correction; example 4, the answer before it, is in `rounds/fixture-runs-v1/report-all-runs.md` — evidence for the reader, not part of what you load, where it shows the folder guessed first too). It also proves the model holds one line by itself: it will not invent a number it has no source for.

**What it does not prove.** That the bare model always guesses; one run. That the scenarios are wrong: the tension it found (structured fields say "ISS inside the Simples", free text says "fixed") is real and is the open question for the office.

---

## B3 — Claude Fable 5.1, effort "high", web on · clean note + profile line (`transcript-B3.md`)

**What came back.** The widest review of the three: everything B1 found, plus real things the folder does not check — the anonymised `Id` attributes not in the layout's numeric format (true; they carry letters and do not start with the municipality code), the "alíquota do Simples" label in the free text, the IBPT figures incoherent with each other, `pAliqAplic` absent, leading zeros in the numbers, no signature, and an emission-channel deadline taken from a CGSN resolution found on the web. Corrections advised throughout. On "continue", it wrote a validator script (493 lines) that reproduces its own verdicts (5 failures, 7 warnings, 14 passes, by its own count).

**What it proves.** A stronger model with the web covers more of the layout and the law than the folder does, and finds defects in these fixtures the folder's checks are blind to. Two of them are now candidate checks (`regEspTrib` coherent with the regime; the `Id` format) and one is a finding about the anonymiser (`fixtures/README.md`). The gap in domain coverage between "no folder" and "folder" is real and it is not small.

**What it does not prove.** That any of it is verifiable here: no report rows; the CGSN resolution and its dates are not in the folder and were not checked (they may be right; a reader of this repository cannot tell). That it refrains from deciding: it prescribed corrections and then built a tool around its own opinion. That its validator is an auditor in the brief's sense: it cites articles by number, not text a reader can open.

---

## Conclusion, plainly

Across the three runs, the model without the folder **knows more law than the folder checks**, and it found real things the folder misses. What it did not do in any run is the four things the folder was built for:

1. **Give the reader something to check.** No run produced a row a script can open against the standard; the quotes mix verbatim, reworded and web-only text. The brief's own words: an auditor that cannot cite the standard is an opinion generator.
2. **Stop where a fact is missing.** B5 supplied the client's regime from the note's free text and rewrote the note on it; the folder says CANNOT DETERMINE.
3. **Hand the decision back.** All three prescribed corrections; B5 wrote the corrected XML; B3 wrote a tool. The folder's refusal transcript hands the decision back three times.
4. **Come back the same shape every time.** The folder returns six checks, four results, one order, on every note — comparable across months and clients, and its own run-to-run variance is recorded (`fixture-runs-v1/what-changed.md`, row 9).

So the folder is not "a model that knows ISS". It is the layer that turns a capable model into an instrument whose output a stranger can verify and an operator can trust without re-reading the law. What the bare runs contribute to it is a list of checks it should have — recorded as candidates, to be added in a dated commit after the office answers the open questions — not a reason to skip the layer.

**On cost, and what it means at scale.** Every run of the folder in `examples.md` was made on Claude Opus 4.8 at low effort, and every report came back checkable; no other setting was tried with the folder. The bare model at the same setting (B1) was competent but not checkable; the bare run that covered the most ground (B3) used Claude Fable 5.1 at high effort, with web search, and was still not checkable. So what makes a report checkable is the folder, not the size of the model. For an office that closes the books for dozens of clients a month, the setting a checkable report needs is what decides whether the folder can run on every note; the cost per report itself was not measured. Not measured either: a smaller model (Sonnet) with the folder, and the folder on Fable 5.1.

**What this control as a whole does not prove.** One run per condition; the author chose the request; web results change by the day; low effort on two of the three runs. It does not rank models, and it does not say the folder's six checks are the right six — the bare runs are the argument that they are not enough.
