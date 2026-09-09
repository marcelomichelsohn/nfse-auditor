# Bare model — what this shows (written 2026-09-09 after B1, B5 and B3, from the transcripts and the checker)

**The question.** Without the folder — the model with everything it can do on its own, web search included — what does a plain request return, next to what the folder returns on the same input? Three runs (`transcript-B1.md`, `transcript-B5.md`, `transcript-B3.md`); the predictions and the condition (web on) are in `expected.md`.

## What the bare model did

| Run | Input | What came back |
|---|---|---|
| B1 — Opus 4.8 low, web on | clean note + profile line | A competent prose review: incidence, code, Simples flags, retention and values right; did **not** fall for the municipal rate table (it read the IBPT figures as informational — prediction 2 of `expected.md` was wrong). Flagged `regApTribSN = 1` against the profile's fixed ISS as a **failure with a correction written out**, and `regEspTrib = 0` (a field the folder does not check). Ended with what it could not verify. |
| B5 — Opus 4.8 low, web on | clean note, **no profile line** | Read the regime from the note's free text ("Fixo Contador") and **rewrote the note**: an XML snippet to paste, a new observations text, an offer to fill in the fixed amount and recompute the net value. Refused only to invent the municipal amount. The folder on the same input: CANNOT DETERMINE on the four checks that need the registration (`examples.md`, example 4b). |
| B3 — Fable 5.1 high, web on | clean note + profile line | The widest review: everything B1 had, plus the anonymised `Id` attributes not in the layout's numeric format (true — a finding about these fixtures), the "alíquota do Simples" label, the IBPT figures incoherent with each other, `pAliqAplic` absent, leading zeros, no signature, and an emission-channel deadline from a CGSN resolution found on the web. Corrections advised throughout. On "continue", wrote a 493-line validator that reproduces its own verdicts. |

## Measured

- **Checkable rows:** `tools/check_audit.py` found **no report rows** in any of the three answers (the control count stayed at the 8 rows of `control-no-reference/`): there is no table to check, so no quote can be opened against a provision in the folder.
- **Citations of B1 tested against the folder's standard** (whitespace-normalised substring): the §22-A sentence — found verbatim; the layout rule on `regApTribSN` — reworded ("deixa de apurar… atribui" for "deixará de apurar… atribuir"), not found; the CGSN sentence and the emitter's retention rule — not in the folder, from the web.
- **Advice:** B1, B5 and B3 all wrote corrections; B5 wrote the corrected XML. The folder's refusal transcript (`rounds/refusal/`) hands the decision back three times on the same kind of request.

## What this shows, plainly

The folder does not add knowledge. The bare model, with the web, covered more of the law than the folder's six checks and found real things the folder does not look at — `regEspTrib`, the `Id` format, the labels in the free text. Two of those are now candidate checks (see `fixture-runs-v1/what-changed.md`, row 13). What the folder adds is elsewhere:

1. **Checkability.** Every quote in a folder report opens in `reference/` and is checked by a script; the bare model's citations mix verbatim, reworded and web-only text a reader of this repository cannot open. An audit a stranger cannot verify is an opinion (the brief's own words).
2. **Not guessing.** Given a note without the client's registration, the folder says CANNOT DETERMINE where the fact is missing; the bare model supplied the fact from the note's own free text and rebuilt the note on it.
3. **Not deciding.** The folder reports and hands back; the bare model corrects, rewrites and offers to recompute.
4. **The same shape every time.** Six checks, four results, one order — the office's assistant gets the same table on every note, and the run-to-run variance of the folder itself is recorded (`fixture-runs-v1/what-changed.md`, row 9).

## What this does not prove

One run per condition; the author chose the request; web results change by the day (the CGSN dates B3 cites were not verified against the folder, because they are not in it); low effort on two of the three runs. It does not rank models and does not say the folder's checks are the right six — the bare model's findings are the argument that they are not enough.
