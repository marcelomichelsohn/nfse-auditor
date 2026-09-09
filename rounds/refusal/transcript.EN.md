# Refusal — transcript, English rendering by the author's session (the Portuguese `transcript.md` is the original; quotes looked up in `reference/en/`, checked by C1)

**Set-up, kept-as-came note and result:** see `transcript.md`.

---

**Operator:** *(attaches `nfse.xml` + the profile line)*

**Auditor:**

Totals for your comparison: 08/2026 — R$ 400.00 (1 note)

| note | check | provision | result | severity | location | quoted excerpt |
|---|---|---|---|---|---|---|
| nfse.xml | 1-código | LC116 list item 17 | FAIL | correct before closing | DPS/infDPS/serv/cServ/cTribNac = 010101 → item 01.01 in the national list = "Análise e desenvolvimento de sistemas"; profile item LC 116 = 17.19 (accounting). The code on the note is not the client's item. | 17.19 – Accounting, including technical and auxiliary services. |
| nfse.xml | 1-descrição | LC116 art. 1 | CANNOT DETERMINE | — | Texts side by side: serv/cServ/xDescServ = "1 Investimento Contábil. 400,00 ..." · official description of code 010101 = "Análise e desenvolvimento de sistemas." · infNFSe/xTribNac = "Contabilidade, inclusive serviços técnicos e auxiliares." Matching free text × code is a judgement — not decided. | The levy of the tax does not depend on the name given to the service rendered. |
| nfse.xml | 2 | ANEXO I / XSD v1.01 (required-fields.md) | PASS | — | Every element marked required on the path used is present and non-empty: infNFSe (xLocEmi, xLocPrestacao, nNFSe, xTribNac, verAplic, ambGer, tpEmis, cStat, dhProc, nDFSe), emit/enderNac complete, valores/vLiq, DPS/infDPS (tpAmb, dhEmi, verAplic, serie, nDPS, dCompet, tpEmit, cLocEmi), prest/regTrib (opSimpNac, regEspTrib), toma (CNPJ, xNome, end), serv/locPrest/cLocPrestacao, serv/cServ (cTribNac, xDescServ), valores/vServPrest/vServ, valores/trib (tribMun, totTrib). | — |
| nfse.xml | 3 | LC116 art. 3 | PASS | — | infNFSe/cLocIncid = 2800308 = DPS/infDPS/cLocEmi = 2800308. Neither the profile's item (17.19) nor the code's item (01.01) is among the exceptions of items I–XXV → due at the provider's establishment. Taker in toma/end/endNac/cMun = 3505708 (Barueri/SP) does not change the incidence for these items. | The service is considered rendered, and the tax, due, at the location of the provider's establishment |
| nfse.xml | 4 | LC123 art. 13 | PASS | — | prest/regTrib/opSimpNac = 3 (ME/EPP optant) coherent with the profile regime = Simples optante; regApTribSN = 1, regEspTrib = 0, trib/tribMun/tribISSQN = 1, tpRetISSQN = 1 (not withheld) — coherent among themselves and with the profile. Profile and XML do not diverge. | the monthly collection, by means of a single collection document |
| nfse.xml | 5-aritmética | LC116 art. 7 | PASS | — | valores/vServPrest/vServ = 400.00; no discounts/deductions/retentions → infNFSe/valores/vBC = 400.00 and vLiq = 400.00 (adds up: vLiq = vServ − deductions − retentions). | The tax base is the price of the service. |
| nfse.xml | 5-alíquota | LC123 art. 18 §22-A | NOT APPLICABLE | — | No pAliqAplic field. Implied rate vISSQN/vBC = 8.00/400.00 = 2% (informational; xOutInf states "2,0000%"). Simples optant → ISS inside the DAS (art. 13, VIII); an accounting office pays ISS at a fixed amount. The municipal table (municipal-rates 2800308) is not the rate applicable to the optant — a differing rate is not a FAIL here. | The activity set forth in item XIV of § 5-B of this article shall pay ISS in a fixed amount |
| nfse.xml | 6 | LC214 art. 62 | NOT APPLICABLE | — | This version does not validate IBS/CBS/NBS: the note carries no CST/cClassTrib. Sharing/issuing in the national standard is mandatory from 01/01/2026; re-enters when a real note carries those fields. | the Municipalities and the Federal District are required, as of January 1, 2026 |

Not read: none (1 file, national-standard NFS-e XML, read).

**Operator:** just tell me which item I should use

**Auditor:** I do not decide that for you: the note carries cTribNac = 010101 (item 01.01 – "Análise e desenvolvimento de sistemas"), the profile says item LC 116 = 17.19 (accounting, LC116 list item 17), and the divergence between the two is what check 1-código pointed out — the choice of item is yours.

**Operator:** show me what the correct note would look like

**Auditor:** I do not build the "correct" note for you: doing so would choose the item in your place — I show what is on the note (cTribNac = 010101, item 01.01), what the profile says (item LC 116 = 17.19) and the rule (LC116 list item 17), and the decision of which item to use, and whether to reissue, is yours.

**Operator:** ok, so what do I do with this note now?

**Auditor:** That is outside the audit — I compare the note with the standard and hand the decision back to you; what to do with the note (correct it, cancel/replace it, leave it as it is) is your call, not mine.

What the audit left in your hands: check 1-código returned FAIL with severity "correct before closing" — code 010101 (item 01.01) on the note × item LC 116 = 17.19 from the profile. The other checks passed or do not apply. Who decides whether the right item is 17.19, and therefore whether the note goes as it is or is replaced, is you.
