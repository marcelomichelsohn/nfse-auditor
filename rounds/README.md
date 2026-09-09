# rounds/ — the witnessed trail

This folder is evidence, not instructions. The auditor never loads it. A reader opens it to check that real people used the folder, in the order the commits say.

## Roles
The single table of who is who in this repository. Every transcript, request, protocol, commit message and README uses these labels and no other.

| Label | Who |
|---|---|
| **Manager** | the owner of the accounting office; chose the standard and the clients; reviews the Employee's work (step 6 of the office's process) |
| **Employee** | the fiscal assistant of the office; does the monthly closing (steps 2–5 and 7); runs the rounds |
| **Marcelo** | the author of this repository; a client of the office; present at every round; transcribes and builds |
| **Support** | the office's customer-service person; asks each client the month's revenue in the first days of the month (step 1); does not appear in the group |
| **Partner** | the Manager's business partner in the office — she runs the accounting, he runs the legal side; a member of the group; spoke once, to agree to the publication (`CONSENT.md`) |

Real names, the office's name, client names, CNPJs, e-mails and phones do not appear anywhere in this repository.

Consent — what was asked, what was agreed, when — is in `CONSENT.md`, with the verbatim lines and dates. In one line: captures of the rounds agreed 07/09; publication of the conversation, without names or confidential data, asked and agreed 08/09 16:15–16:18; third-party client notes only after the office's confidentiality agreement.

## Protocol
`PROTOCOL.md` — written and committed before any round. A change is a new dated section, never an edit.

## Rounds
| Folder | What | Status |
|---|---|---|
| `fixture-runs-v1/` | the author's runs on the fixtures (09/09): `what-changed.md` lists, in order, what each run showed and what changed in the folder because of it, with the commit — the reports themselves are `examples.md` | living; one row per change |
| `control-no-reference/` | the same clean note fed to the folder loaded **without** `reference/` — what the model does when the standard is not in the folder; the checker's unresolved count is the measure | `expected.md` committed 09/09 08:42; `transcript.md` 09/09 ~12:55 — the model left the quote column empty rather than invent; `what-this-shows.md` carries the checker's count |
| `control-bare-model/` | the same note and profile line in a plain chat, no folder at all — what any capable model does on its own, next to what the folder does | `expected.md` committed 09/09 ~13:15; runs pending |
| `refusal/` | three disguised requests for advice after a real audit, in the operator's voice; the auditor must hand the decision back | `expected.md` committed 09/09 08:42; `transcript.md` 09/09 ~12:40 — handed back on all three; `transcript.EN.md` beside it |
| `round-0-by-hand/` | the Employee closes Marcelo's own company by hand, no system — the baseline (its notes exist only as the municipality's fixed-width text export, not XML) | `REQUEST.md` committed 08/09; recording received 08/09 16:28 → `transcript.md`, `time.md` |

Each round folder, when complete: `expected.md` (committed before the run) · `transcript.md` · `time.md` · `what-changed.md`. This table is updated when a round lands; what failed and what changed in the folder is written here, dated.

## Order proof
`ORDER-PROOF.md` — output of `../tools/prove_order.py`, written at every close: each round's prediction precedes its transcript, round N precedes N+1, the public remote holds exactly the local commits, and a fresh clone reproduces the history.
