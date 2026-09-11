# Bare model, run B1 — transcript, English rendering by an agent (the Portuguese `transcript-B1.md` is the original and governs wherever the two differ)
**Translation by an agent, declared as such. This is a control run with no folder: the model's citations point to sources outside this repository, and none of them is a `reference/` quote; they are translated as they came, not looked up.**

**Conditions:** Claude Opus 4.8, effort "low"; a plain conversation outside any project; the XML attached, the profile line pasted, the fixed request of `expected.md`; **4 min 50 s** by the author's clock. *(Whether web search was on in that chat: see the note at the end.)* Kept as it came.

---

**Operator:** *(attaches `nfse-01.xml`, pastes the profile line and the request of `expected.md`)*

**Model:**

Checked the XML against the three standards. Verdict in short: the **territorial incidence is correct**, but the **ISS classification is inconsistent with the "anexo fixo" registration** — the note pays the ISS as a percentage inside the Simples, and not as a fixed amount. Below I set out what fails and what passes, with the "where" (XML tag), the provision and the risk/confidence rating.

---

## What FAILS

**1. ISS assessed inside the Simples (2%) instead of a fixed amount**
*Where:* `DPS/infDPS/prest/regTrib/regApTribSN = 1` and, as a consequence, `infNFSe/valores/vBC = 400,00` with `vISSQN = 8,00` (2%). The `xOutInf` confirms it: "Simples Nacional rate: 2,0000%".

In the national layout, `regApTribSN = 1` means "assessment of the federal **and municipal** taxes under the Simples Nacional" — that is, the ISS goes into the DAS as a percentage. The business rule of Annex I (Layouts and Business Rules of the DPS/NFS-e, SE/CGNFS-e) is explicit: an ME/EPP stops assessing the ISSQN under the Simples Nacional when it assigns the values 2 or 3 to the regApTribSN field. For an accountant who is an optant and pays a fixed amount, the correct value is **`regApTribSN = 2`** (federal taxes under the SN, the ISS outside it, under municipal legislation).

The legal basis for the fixed amount is LC 123/2006, art. 18, § 22-A together with § 5º-B, XIV: the activity listed in item XIV of § 5º-B of this article shall pay the ISS as a fixed amount, in the manner set by municipal legislation (item XIV is accounting-services offices). And the practical effect, confirmed by the CGSN's guidance: in this case the ISS will not be included in the PGDAS. Here it is being included — which therefore contradicts the "anexo fixo" registration.

- **Risk: high** · **Confidence: high** (on the layout rule and on the law) / **medium** (on the application to this particular case — it depends on the item to be verified below).
- **Party affected:** the direction depends on the municipal fixed amount against the turnover. If Aracaju's fixed amount is lower than 2% of the monthly turnover, the note **harms the taxpayer** (it pays ISS in excess); if it is higher, it **harms the tax authority**. In either scenario, it exposes the provider to amendment or assessment for a wrongly declared regime.
- **Fix:** `regApTribSN` → `2`; the ISS stops going out in the DAS and starts being paid on a municipal slip (DAM) as a fixed amount. `vISSQN` on the note stops reflecting the 2% assessed under the SN.

**2. Special tax regime not flagged**
*Where:* `DPS/infDPS/prest/regTrib/regEspTrib = 0` (None).

For a legal entity that pays the ISS as a fixed amount — the typical example being an accounting office — the national layout provides for `regEspTrib = 6` (Society of Professionals). The official guidance of BH/CRC-MG lists code 6 – Society of Professionals, intended for Societies of Liberal Professionals, and the integration documentation of the national issuer is direct: legal entities under a Fixed ISS collection regime — example: an accounting office — must send the regEspTrib tag with the value 6.

- **Risk: medium** · **Confidence: medium** (the requirement of `regEspTrib = 6` combined with being a Simples optant may vary with how the municipality of incidence is configured; some validate it, others expect the fixed amount to come through `regApTribSN` alone).
- **Party affected:** the taxpayer — the omission strips the documentary evidence of the uniprofessional/fixed classification and may cause a rejection ("Special regime not allowed for the provider…") or taxation as an ordinary service.
- **Fix:** `regEspTrib` → `6`, aligned with `regApTribSN = 2`.

**3. Tax base and ISS amount filled in as an ordinary transaction**
*Where:* `infNFSe/valores/vBC = 400,00` and `vISSQN = 8,00`.

It is a symptom of items 1 and 2: under the fixed amount, the ISS is not calculated on the service value of the note. Once `regApTribSN` and `regEspTrib` are corrected, these fields stop expressing 2% on R$ 400.

- **Risk: medium** · **Confidence: high** (it is an arithmetic consequence of the items above). **Party affected:** the taxpayer.

---

## What PASSES

**Municipality of incidence (the most sensitive point, and it is right).** `infNFSe/cLocIncid = 2800308` (Aracaju), the same as the provider's establishment, even with the taker in Barueri/SP (`toma/end/endNac/cMun = 3505708`). Accounting (17.19) is **not** among the exceptions of items I–XXV of art. 3 of LC 116/2003, so the general rule applies: ISS due at the provider's establishment. The note did **not** shift the incidence to the taker — correct. · *Risk of error: none · Confidence: high.*

**Service code.** `cServ/cTribNac = 171901` maps to subitem 17.19 of LC 116, and `xTribNac`/`xTribMun` carry "Accounting, including technical and auxiliary services" — consistent with the profile (CNAE 6920-6/01, LC 116 17.19). · *Confidence: high.*

**Status under the Simples.** `regTrib/opSimpNac = 3` (ME/EPP optant) matches the "Simples optante" registration. · *Confidence: high.*

**ISS taxation/withholding.** `tribISSQN = 1` (taxable transaction) is coherent with "exporta não". `tpRetISSQN = 1` (not withheld) is coherent — the ISS being due in Aracaju, the taker in Barueri does not withhold. The national issuer's own rule: tribISSQN with the value 1 and tpRetISSQN with the value 1 will be treated as withheld tax "No". · *Confidence: high.*

**Coherence of the amounts.** `vServ = vBC = vLiq = 400,00`, with no deductions (`vCalcDR = 0,00`). Sound in its arithmetic (the only caveat is `vISSQN`, dealt with above). The R$ 53,80 of federal and R$ 20,00 of municipal taxes in `xOutInf`/`totTrib` are the **approximate IBPT** figure (Law 12.741/2012, transparency), merely informative — it is not the real ISS, so the divergence between the R$ 20 of the IBPT and the R$ 8 of the note is not, in itself, an error.

---

## What needs to be verified to close the diagnosis

The whole contradiction turns on **a fact of municipal law that I cannot confirm from here**: does Aracaju's legislation grant (and does this accountant qualify for) the ISS as a **fixed amount**?

What I was able to verify of Aracaju's Municipal Tax Code: it sets the minimum ISS rate at 2% (art. 103-A) and has a uniprofessional-society regime with exclusion criteria (an unqualified partner, a capital-only partner, the existence of a branch and so on). That is, the 2% on the note is exactly Aracaju's **ordinary minimum** — which reinforces that the note was issued as an ordinary service, not as a fixed amount.

Two honest readings:

- **If the "anexo fixo" registration is correct** (Aracaju authorises the fixed amount and the office meets the strictly personal requirements — recent case law of the STJ, REsp 2.162.486/SP, admits even an LTDA provided it renders personal service, with no business structure): then the **note is wrong** in items 1–3 and must be amended.
- **If Aracaju is silent on / does not authorise the fixed amount for this case**: then the note is right (ISS under Annex III in the DAS, art. 25, § 1º, III of CGSN Resolution 140/2018) and it is the **"anexo fixo" registration that is wrong**.

One way or the other, registration and note are saying different things, and that has to be reconciled.

If you like, I can pull the specific article of Aracaju's CTM on uniprofessional societies/accountants and the law that sets the fixed amount, to settle which of the two readings holds — that is what decides whether we correct the note or the registration.
