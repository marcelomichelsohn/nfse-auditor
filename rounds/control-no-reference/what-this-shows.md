# Control — what this shows (written 2026-09-09 after the run, from the checker's output)

**The prediction** (`expected.md`): without `reference/` the model would still produce the table, quote the law from memory, and the checker would report the quotes as unresolved.

**What happened** (`transcript.md`): the model produced the table and **did not quote the law at all.** It said why, before the table: the quote column must be verbatim from `reference/pt/excerpts/` and `identity.md` forbids inventing a citation, so it left the column with "(corpus não carregado)". Checks that need a table (`1-código` against ANEXO B, `2` against the layout) came back CANNOT DETERMINE "for lack of corpus, not for lack of data on the note". Checks that need only the XML and the profile line (`3`, `4`, `5-aritmética`, `5-alíquota`, `6`) came back with a result and a location, but no citation.

**The measure, as `tools/check_audit.py` printed it** (control mode — reported, not a gate):

```
CONTROL (rounds/control-*, not a gate): rows 8, C1/C2 findings 12 — the measure of what the folder adds
```

Of the 8 rows, 8 have no resolvable quote (C1) and 4 carry a provision id that is not in `reference/INDEX.md` (C2), because the model wrote the provision labels from `rules.md` instead of the INDEX's "cite as" ids.

**What this shows.** Without the standard in the folder, the report is not checkable: no row can be opened against the provision it cites, which is the brief's own test of an auditor. The two files that stayed loaded (`identity.md`, `rules.md`) were enough to stop the model from inventing a citation — a better outcome than predicted, and worth knowing: the rule "cite verbatim or say you cannot" held even with nothing to cite from. What makes the report checkable is `reference/`; what stops it from bluffing is the rules.

**What this does not prove.** One note, one run, one model at low effort. It does not prove the runs with `reference/` loaded are correct — `expected/` and the rounds do that. It does not prove the model would refuse to invent under every phrasing; it shows what it did once, unprompted.
