# fixtures/ — the test documents (anonymised NFS-e XML)

This folder is the verify layer: the auditor never loads it. A reader uses it to re-run an audit and compare with `../expected/`.

## Where they come from
- **`clean/`** — real NFS-e issued in the national standard, anonymised by `../tools/anonymise.py` and reviewed one by one by the author before entering. In this version the clean notes are two notes the accounting office issued **to the author's own company** (the author is the taker; his consent covers them). They are the *pass* cases, including the case where the rate on the note differs from the municipal table because the issuer is a Simples Nacional optant paying fixed-amount ISS (NOT APPLICABLE, not FAIL).
- **`mutations/<slug>/`** — a copy of a clean note with **one field changed**, plus `CHANGE.md` saying the field, the value before and after, and the check that must catch it. They exist because the clean notes are all correct: the FAIL cases are made, and the making is written down.
- **`rephrase/`** — the m1 violation (wrong service code) kept, and the free-text description rewritten three ways (`CHANGE.md` there). Each is fed in a conversation of its own: an auditor that fires on one wording and not on the others is reading the phrasing, not the provision. Synthetic, by the author, and said so.
- **`unreadable/`** — a plain-text file that is not an NFS-e, to show the report's "not read" list working.
- **Third-party clients' notes** (with real errors found and corrected by the office) enter only after the office's confidentiality agreement is signed and each file is reviewed by the author; until then, the clean notes above are marked *build fixtures* and are relabelled "superseded on <date>" when a real client note lands.

## What the anonymiser does — the single source of this list (`../tools/anonymise.py` implements it)
| Class | Fields | What happens |
|---|---|---|
| Identity numbers | `CNPJ`, `CPF`, `IM`, `nNFSe`, `nDPS`, `nDFSe`, `cIntContrib`, the `Id` attributes; file names | replaced by synthetic values of the same format (CNPJ/CPF with valid check digits), the same real value always mapped to the same fake across files (mapping kept outside the repo); files renamed `nfse-NN.xml` |
| Names of companies | `xNome`, `xFant` | placeholders: `PRESTADOR CONTABIL LTDA`, `TOMADOR NN LTDA` |
| Addresses | `xLgr`, `nro`, `xCpl`, `xBairro`, `CEP` | generic street, number and district; CEP keeps its first five digits (the locality) and ends in `000` |
| Contacts | `fone`, `email` | fixed fakes |
| Free text | `xDescServ`, `xOutInf` | structure kept (service words, amounts); any mapped name or number inside it replaced; the before/after of every free-text field is read by the author before the file enters |
| People in transcripts | — | not in XML; roles only (`../rounds/README.md` § Roles) |
| **Kept** | `cMun`, `cLocEmi`, `cLocPrestacao`, `cLocIncid`, `UF`; `dhEmi`, `dCompet`, `dhProc`; `vServ`, `vBC`, `vISSQN`, `vLiq`; tax flags (`opSimpNac`, `regApTribSN`, `tribISSQN`, `tpRetISSQN`); `cTribNac`; `verAplic`, `ambGer`, `cStat` | the checks need them; municipality codes are public codes of public bodies |
| `Id` attributes | `infNFSe/@Id`, `infDPS/@Id` | replaced by synthetic values of the same length, **not in the layout's numeric format** (they carry letters and do not start with the municipality code — found by the bare-model control on 09/09/2026, `../rounds/control-bare-model/`); the auditor does not check the `Id` format in this version |
| **Stripped** | the whole `Signature` block | the X.509 certificate carries the real name and CNPJ, and the digests bind to the real content. **Consequence:** the fixtures are not signature-valid, and the auditor does not check signatures in this version |

**Residual risk, said plainly.** A note's date, municipality and amounts survive. For an accounting office in one city that is a small set. The office is not named anywhere in this repository, and the two clean notes are the author's own; the cold audit before the final push decides whether amounts must also be perturbed.
