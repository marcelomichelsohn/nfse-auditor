# Bare model, run B5 — transcript, English rendering by an agent (the Portuguese `transcript-B5.md` is the original and governs wherever the two differ)
**Translation by an agent, declared as such. This is a control run with no folder: the model's citations point to sources outside this repository, and none of them is a `reference/` quote; they are translated as they came, not looked up.**

**Conditions:** Claude Opus 4.8, effort "low"; a plain conversation outside any project, **web search on**; the XML attached, no profile line, the fixed request of `expected.md`. Kept as it came. Prediction: `expected.md` § Addendum, B5.
**What happened, in one line:** with no client registration given, the model read "Fixo Contador" in the note's free text as the client's regime, built two scenarios on it, and **rewrote the note** — an XML snippet to paste, a new observations text, and an offer to fill in the fixed ISS amount and recompute the net value once told the municipal figure. The folder, on the same input, returned CANNOT DETERMINE on the four checks that need the registration (example 4b) and hands decisions back (`rounds/refusal/`). One discipline the bare model did keep: it refused to invent the municipal fixed amount.

---

**Operator:** *(attaches `nfse-02.xml`, no profile line, pastes the request of `expected.md`)*

**Model:**

I am going to settle one detail before handing you the ready-made snippets: I need the exact `regEspTrib` code for the fixed regime, otherwise I hand you a snippet with a guessed number — which goes against the rule of only asserting what can be shown. Let me confirm the official table.Confirmed. The official `regEspTrib` table in the national standard is: 0-None, 1-Cooperative Act, 2-Estimate, 3-Municipal Microenterprise, 4-Notary/Registrar, 5-Self-Employed Professional, 6-Partnership of Professionals. And the mapping of the "fixed-amount accountant" profile fits exactly: an accounting partnership of professionals that is a Simples optant is configured as `opSimpNac = 3`, `regApTribSN = 2` ("federal taxes under the SN and the ISSQN under the NFS-e according to municipal legislation") and `regEspTrib = 6`. That is, the fixed regime has a structural signature of its own — and the note you sent me carries none of the three marks.

Before the snippets, the decision rule. Two facts define which scenario holds:

1. **Does Aracaju have a law setting a fixed ISS amount for accounting services?** § 22-A of LC 123/2006 grants the fixed amount only "in the form of municipal legislation" — with no local law, there is no fixed amount.
2. **Is the company a single-profession partnership (accountant partners only, non-business character) or an ordinary business LTDA?** The STJ tends to deny the fixed amount to a business LTDA that does not qualify as a partnership of professionals. Since the provider is "PRESTADOR CONTABIL **LTDA**", this is the point that decides.

If both answers are "yes" → **Scenario A**. If either is "no" → **Scenario B**.

## Scenario A — the fixed amount is real (an accounting single-profession partnership licensed in Aracaju)

Then the error is in the profile/registration. Replace the `regTrib` group with:

```xml
<regTrib><opSimpNac>3</opSimpNac><regApTribSN>2</regApTribSN><regEspTrib>6</regEspTrib></regTrib>
```

And the values need to change in nature: `vISSQN` stops being 2% of the revenue (R$ 8.00) and becomes the **fixed amount per licensed professional** that Aracaju's law establishes. I am not filling in that number because I do not have the municipal law at hand — putting any value here would be inventing. What can be asserted is that `<vISSQN>8.00</vISSQN>` (computed on `vBC 400,00`) is incompatible with the fixed regime and has to be replaced by the municipal fixed quota.

In `xOutInf`, the line "Alíquota do Simples Nacional: 2,0000%" becomes misleading in this scenario, because under the fixed regime the ISS is not a percentage of the note. I suggest:

```
Optante do Simples Nacional - Sociedade de Profissionais (Contador). ISS recolhido em valor fixo, art. 18, §22-A, LC 123/2006 - legislação municipal de Aracaju. Trib. aprox. R$ 53,80 Federal e R$ 20,00 Municipal. Fonte: IBPT [A906AF].
```

## Scenario B — the "Fixo" label is improper (ordinary business LTDA)

Then the profile is right (`regApTribSN = 1`, `regEspTrib = 0`, ISS at 2% under the Simples) and the error is only the text promising a regime the company does not have. The `regTrib` **stays exactly as it is** — it is not touched. Only the `xOutInf` is corrected, removing "Fixo":

```
Optante do Simples Nacional - Contador. Trib. aprox. R$ 53,80 Federal e R$ 20,00 Municipal. Fonte: IBPT [A906AF]. Alíquota do Simples Nacional: 2,0000%
```

In this scenario nothing else changes: the R$ 8.00 at 2% are correct and at the legal floor (art. 8º-A of LC 116/2003).

---

Summing up the logic: the document's structural fields describe a **percentage** accountant (Scenario B ready to hold), while the free text announces a **fixed-amount** accountant. One of the two is lying. If you tell me whether Aracaju has a fixed ISS for accountants and whether the company is single-profession or a business company, I will tell you for certain which of the two snippets to apply — and, in Scenario A, if you give me the fixed amount from Aracaju's law, I will fill in the `vISSQN` and recompute the `vLiq`.
