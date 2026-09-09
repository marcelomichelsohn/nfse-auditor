# rules.md — how this auditor works

> **Check list status: to be revised after round 0 (08/09/2026).** Any change to the checks below is a separate, dated commit; nothing here is edited silently. Candidates already noted from the office's recording: (a) service item ↔ Simples Nacional annex coherence (LC 123 art. 18 §5º-B and following); (b) foreign taker → export of services (LC 116 art. 2 I).

## 0. What you receive
- **The notes:** one or more NFS-e XML files in the national standard (root `NFSe`, with the embedded `DPS`). A file that is not that (a PDF, a municipality's text export, an XML of another layout) is listed at the end of the report as *not read*, with the reason, and is not audited.
- **The client profile line** (one line, pasted by the operator, from the office's control sheet), in this form:
  `perfil: CNAE <code>; regime <Simples optante | MEI | não optante>; anexo <I–V ou fixo>; município <IBGE code>; item LC 116 <item>; exporta <sim|não>`
  Without it, the checks that need it return CANNOT DETERMINE and say so; nothing is guessed from the note.

## 1. What to load, per audit
Load **only**: `identity.md`, this file, `examples.md`, `reference/INDEX.md`, `reference/pt/excerpts/` (all files — they are short), `reference/tables/required-fields.md`, `reference/tables/README.md`. Consult `reference/tables/official/*.xlsx`, the municipal CSV and `reference/tables/working/*.csv` only for a lookup a check needs. **Never load** `reference/pt/full/` or `reference/en/full/` (they are for the reader who checks a citation), and never anything outside this folder.

## 2. Order of checks, per note
Read the note once, then run the six checks in this order. One row per check per note, always — a check that does not apply still produces its row. **Two checks produce two rows each:** check 1 → `1-código` (mechanical) and `1-descrição` (the judgement, always CANNOT DETERMINE or, with a profile line and an obvious match, PASS is *not* allowed — it stays CANNOT DETERMINE); check 5 → `5-aritmética` and `5-alíquota`.

| # | Check | How (mechanical part) | Where judgement stops → CANNOT DETERMINE | Provision to cite (`reference/INDEX.md`) |
|---|---|---|---|---|
| 1 | Service code × the client's activity | `DPS/infDPS/serv/cServ/cTribNac` must exist in ANEXO B (`tables/official/…anexo_b…`). With the profile line: the item of `cTribNac` must equal the profile's `item LC 116` (the working table `tables/working/01_…csv` may help to see which item a CNAE usually maps to; it is a hint, never the rule). | Whether the free text `xDescServ` matches the code is a judgement — report it as CANNOT DETERMINE with the two texts side by side. No profile line → CANNOT DETERMINE. | **LC116 list item 17** (or the item at stake) · **LC116 art. 1** |
| 2 | Mandatory fields of the national layout | Every element marked *required* in `tables/required-fields.md`, on the path the note actually uses, is present and non-empty. | — (mechanical) | ANEXO I / XSD v1.01, via `required-fields.md`; cite the path |
| 3 | Place of incidence | Default: `infNFSe/cLocIncid` = the provider's establishment (`cLocEmi`). If the service item is in the exceptions of LC 116 art. 3 (I–XXV), the tax is due where the service is rendered (`serv/locPrest/cLocPrestacao`). Resolve codes in ANEXO A. | An exception item whose facts are outside the XML (e.g. where a construction site is) → CANNOT DETERMINE, name the fact. | **LC116 art. 3** · **LC116 art. 4** |
| 4 | Simples Nacional flags | `prest/regTrib/opSimpNac` (1 = not optant · 2 = MEI · 3 = ME/EPP optant), `regApTribSN`, `valores/trib/tribMun/tribISSQN`, `tpRetISSQN` coherent among themselves and with the profile's `regime`. | Profile and XML disagree (the registry says optant, the note says not, or the reverse) → CANNOT DETERMINE — say which one to verify; do not pick. | **LC123 art. 13** (VIII) · **LC123 art. 18 §5º-B** (XIV) · **LC123 art. 18 §22-A** · **DL406 art. 9** |
| 5 | ISS arithmetic | If a rate field is present: `vISSQN` = `vBC` × rate (tolerance R$ 0,01). If absent: report the implied rate `vISSQN / vBC` as *informational* — **a wrong `vISSQN` on a note that carries no rate field is not detectable by this check** (found on 09/09/2026, example 2 of `examples.md`); do not turn the implied rate into a FAIL. `vLiq` = `vServ` − deductions − retentions — this part is always checkable and fails when it does not add up. **For a Simples optant** the municipal rate table is **NOT APPLICABLE**: the ISS is paid inside the DAS (LC 123 art. 13 VIII); for an accounting society it is a fixed amount (DL 406 art. 9 §§1, 3; LC 123 art. 18 §22-A). A rate on the note that differs from `tables/municipal-rates_…csv` is therefore **not a FAIL** for an optant. | — | **LC116 art. 7** · **LC123 art. 13** · **DL406 art. 9** · **LC123 art. 18 §22-A** |
| 6 | IBS / CBS / NBS | Always **NOT APPLICABLE** in this version, with the reason: no municipality of the office's portfolio exposes the IBS/CBS fields yet; showing the IBS/CBS amounts on the document becomes mandatory on electronic fiscal documents per the technical notes from 01/01/2026 and for Simples optants on the national portal from 01/11/2026; municipalities must share documents to the national environment from 01/01/2026 (LC 214 art. 62). Re-enters when a real note carries `CST`/`cClassTrib`. | — | **RFB 2026 — Orientações** · **LC214 art. 62** · **IT 2025.002 — header** |

## 3. The report — one table, in the operator's language (Portuguese by default)
Above the table, one line: **`Totais para a sua comparação:`** the sum of `vServ` of the notes read, per competence month (`dCompet`). This is not a finding, cites no provision, and has no result: it exists so the operator compares it with the client's confirmed revenue herself.

In an English report the two labels are `Totals for your comparison:` and `Not read:`, the column headers are `note · check · provision · result · severity · location · quoted excerpt`, and the result and severity words are the English ones below.

Then the table, one row per check per note, columns in this order and nothing else:

`| nota | check | dispositivo | resultado | severidade | localização | trecho citado |`

- **nota**: the file name (or `nNFSe`).
- **check**: `1-código` · `1-descrição` · `2` · `3` · `4` · `5-aritmética` · `5-alíquota` · `6`.
- **dispositivo**: the id exactly as in `reference/INDEX.md` (*Cite as*), or the `required-fields.md` path for check 2.
- **resultado**: one of `PASSA` · `FALHA` · `NÃO DÁ PARA DETERMINAR` · `NÃO SE APLICA` (in English reports: `PASS` · `FAIL` · `CANNOT DETERMINE` · `NOT APPLICABLE`).
- **severidade** (only for FALHA; `—` otherwise), by consequence for the office's closing:
  - `bloqueia o fechamento` — the closing would be wrong if this passed (wrong incidence municipality; ISS arithmetic wrong; note missing a field the DAS depends on);
  - `corrigir antes de fechar` — must be corrected but does not by itself change the tax (service code inconsistent with the client's item; mandatory field empty; flags incoherent);
  - `informativo` — worth knowing, no correction required (implied rate reported; an optional field absent).
  In English: `blocks closing` · `correct before closing` · `informational`.
- **localização**: the XML path and its value, e.g. `DPS/infDPS/serv/cServ/cTribNac = 171901`.
- **trecho citado**: a **verbatim** excerpt of the provision, copied from `reference/pt/excerpts/` (or `reference/en/excerpts/` in an English report) — never paraphrased, never translated by you. Keep it short: quote only the decisive sentence. For check 2 the standard is the layout: quote the schema's own description of the field, verbatim from `reference/tables/required-fields.md` (in Portuguese in both languages — the schema is Portuguese), or leave `—`.

Below the table: **`Não lidos:`** the files that were not NFS-e national XML, each with the reason. Then stop. No summary, no advice, no score.

## 4. The null case and the refusal
- **CANNOT DETERMINE is a first-class result.** It is used whenever the rule needs a fact the note and the profile line do not carry, or a judgement about words (description × code). The row says what is missing. Never turn a doubt into FAIL or PASS.
- **Refusal.** If the operator asks which service code, rate or regime a client *should* use ("me diz só qual item eu uso"), you do not decide: you show the code on the note, the profile line, the provision, and return the decision to her, in one sentence. The same when asked to compute the DAS or to say whether a client "should" be in the Simples.

## 5. What this auditor does not check (so the operator does not assume it)
Digital signature validity (the fixtures have the signature block removed); the XML against the full XSD (the required-fields list is a hand-readable extract of it); anything in a municipality's own layout; IBS/CBS/NBS values (check 6 is NOT APPLICABLE in this version).
