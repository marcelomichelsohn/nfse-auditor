# Control — transcript, English rendering by the author's session (the Portuguese `transcript.md` is the original; the quote column carried no citations, so there is nothing to look up)

**Operator:** *(attaches `nfse-01.xml` + the profile line)*

**Auditor:**

Marcelo — before the table, a warning that changes how you read the result: **in this project only `identity.md` and `rules.md` are loaded.** The `reference/` corpus (INDEX, excerpts, ANEXO A/B, `required-fields.md`, municipal/working CSVs) and `examples.md` are not in the mount. I searched the whole filesystem — they do not exist here.

Direct consequence under the auditor's own rules:

- The **`quoted excerpt`** column requires text **verbatim** from `reference/pt/excerpts/`, "never paraphrased, never translated by you" (rules.md §3) — and identity.md forbids inventing a citation. Without the excerpts, **I do not fill that column** (I will not fabricate the legal text).
- **Check 1-código** (existence of `171901` in ANEXO B) and **check 2** (required fields vs. `required-fields.md`) depend on tables that are not loaded → they are **CANNOT DETERMINE** for lack of corpus, not for lack of data on the note.
- **`provision`** should come from the "Cite as" of `reference/INDEX.md`; below I use the provision label as it appears in rules.md and flag that the exact id depends on the INDEX.

What I **can** determine safely from the XML + the profile line runs normally. Here is what can be done, marked honestly.

**Totals for your comparison:** 2026-08 (dCompet 2026-08-31) → **R$ 400.00** (1 note read).

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse-01.xml | 1-código | LC116 art. 1 · item 17.19 | CANNOT DETERMINE | — | `DPS/infDPS/serv/cServ/cTribNac = 171901` | *(corpus not loaded — ANEXO B absent; the code's item = 17.19, **equal** to the profile, but I do not confirm the code exists without the table)* |
| nfse-01.xml | 1-descrição | LC116 list item 17 | CANNOT DETERMINE | — | `xDescServ = "1 Investimento Contábil. 400,00…"` vs `xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares."` | *(a judgement about words — CANNOT DETERMINE by design)* |
| nfse-01.xml | 2 | ANEXO I / XSD v1.01 | CANNOT DETERMINE | — | note populated and well-formed on manual inspection | *(corpus not loaded — `required-fields.md` absent; I do not confirm the list of required fields)* |
| nfse-01.xml | 3 | LC116 art. 3 · art. 4 | PASS | — | `cLocIncid = 2800308` (Aracaju) = `cLocEmi = 2800308`; item 17.19 outside the exceptions of art. 3 | *(corpus not loaded)* |
| nfse-01.xml | 4 | LC123 art. 18 §22-A · DL406 art. 9 | PASS | — | `prest/regTrib/opSimpNac = 3` (ME/EPP optant) coherent with profile "Simples optante"; `regApTribSN = 1`; `tribISSQN = 1`; `tpRetISSQN = 1` | *(corpus not loaded)* |
| nfse-01.xml | 5-aritmética | LC116 art. 7 | PASS | — | `vLiq = 400.00` = `vServ 400.00` − 0 deductions − 0 retentions (`tpRetISSQN=1`) | *(corpus not loaded)* |
| nfse-01.xml | 5-alíquota | LC123 art. 13 · art. 18 §22-A · DL406 art. 9 | NOT APPLICABLE | — | Simples optant, fixed annex (accounting society); ISS not by the municipal table. Implied rate `vISSQN 8.00 / vBC 400.00 = 2.0%` — informational, not a FAIL | *(corpus not loaded)* |
| nfse-01.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | note without `CST`/`cClassTrib` | *(corpus not loaded)* |

**Not read:** none. The file is a national-standard NFS-e XML (`NFSe` version 1.01 with embedded `DPS`).

A content note, separate from the result above: the only thing that caught my eye on manual inspection is `tpRetISSQN = 1` (not withheld) coexisting with `xDescServ` starting with "**1 Investimento Contábil**" — a description × code divergence that is exactly what 1-descrição returns as indeterminable. Not a finding; it is the reason the row exists.

If you want the **complete, citable** table (verbatim `quoted excerpt` column, existence in ANEXO B, a real check 2), the way is to load `reference/` into the project. Do you want me to run again as soon as you upload the corpus, or would you rather I detail now which minimum subset of files unlocks each check?
