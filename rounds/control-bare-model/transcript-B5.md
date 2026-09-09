# Bare model, run B5 — `nfse-02.xml` (clean) with NO profile line, plain chat, no folder (2026-09-09 ~14:00)

**Conditions:** Claude Opus 4.8, effort "low"; a plain conversation outside any project, **web search on**; the XML attached, no profile line, the fixed request of `expected.md`. Kept as it came. Prediction: `expected.md` § Addendum, B5.
**What happened, in one line:** with no client registration given, the model read "Fixo Contador" in the note's free text as the client's regime, built two scenarios on it, and **rewrote the note** — an XML snippet to paste, a new observations text, and an offer to fill in the fixed ISS amount and recompute the net value once told the municipal figure. The folder, on the same input, returned CANNOT DETERMINE on the four checks that need the registration (example 4b) and hands decisions back (`rounds/refusal/`). One discipline the bare model did keep: it refused to invent the municipal fixed amount.

---

**Operator:** *(attaches `nfse-02.xml`, no profile line, pastes the request of `expected.md`)*

**Model:**

Vou fechar um detalhe antes de te entregar os trechos prontos: preciso do código exato de `regEspTrib` para o regime fixo, senão te entrego um snippet com número chutado — o que contraria a regra de só afirmar o que dá para mostrar. Deixa eu confirmar a tabela oficial.Confirmado. A tabela oficial de `regEspTrib` no padrão nacional é: 0-Nenhum, 1-Ato Cooperado, 2-Estimativa, 3-Microempresa Municipal, 4-Notário/Registrador, 5-Profissional Autônomo, 6-Sociedade de Profissionais. E o mapeamento do perfil "contador fixo" fecha certinho: uma sociedade de profissionais contábil optante do Simples é configurada como `opSimpNac = 3`, `regApTribSN = 2` ("tributos federais pelo SN e o ISSQN pela NFS-e conforme a legislação municipal") e `regEspTrib = 6`. Ou seja, o regime fixo tem uma assinatura estrutural própria — e a nota que você me mandou não tem nenhuma das três marcas.

Antes dos trechos, a regra de decisão. Dois fatos definem qual cenário vale:

1. **Aracaju tem lei fixando valor de ISS para o serviço contábil?** O § 22-A da LC 123/2006 só concede o fixo "na forma da legislação municipal" — sem lei local, não há fixo.
2. **A empresa é sociedade uniprofissional (só sócios contadores, caráter não-empresarial) ou uma LTDA empresária comum?** O STJ tende a negar o valor fixo a LTDA empresária que não se enquadre como sociedade de profissionais. Como o prestador é "PRESTADOR CONTABIL **LTDA**", esse é o ponto que decide.

Se as duas respostas forem "sim" → **Cenário A**. Se qualquer uma for "não" → **Cenário B**.

## Cenário A — o fixo é real (SUP contábil habilitada em Aracaju)

Aí o erro está no perfil/cadastro. Substituir o grupo `regTrib` por:

```xml
<regTrib><opSimpNac>3</opSimpNac><regApTribSN>2</regApTribSN><regEspTrib>6</regEspTrib></regTrib>
```

E os valores precisam mudar de natureza: `vISSQN` deixa de ser 2% da receita (R$ 8,00) e passa a ser o **valor fixo por profissional habilitado** que a lei de Aracaju estabelece. Não preencho esse número porque não tenho a lei municipal à mão — colocar qualquer valor aqui seria inventar. O que dá para afirmar é que `<vISSQN>8.00</vISSQN>` (calculado sobre `vBC 400,00`) é incompatível com o regime fixo e tem de ser trocado pela quota fixa municipal.

No `xOutInf`, a linha "Alíquota do Simples Nacional: 2,0000%" fica enganosa nesse cenário, porque no fixo o ISS não é percentual da nota. Sugiro:

```
Optante do Simples Nacional - Sociedade de Profissionais (Contador). ISS recolhido em valor fixo, art. 18, §22-A, LC 123/2006 - legislação municipal de Aracaju. Trib. aprox. R$ 53,80 Federal e R$ 20,00 Municipal. Fonte: IBPT [A906AF].
```

## Cenário B — o rótulo "Fixo" é indevido (LTDA empresária comum)

Aí o perfil está certo (`regApTribSN = 1`, `regEspTrib = 0`, ISS a 2% pelo Simples) e o erro é só o texto que promete um regime que a empresa não tem. O `regTrib` **fica exatamente como está** — não se mexe. Corrige-se apenas o `xOutInf`, removendo "Fixo":

```
Optante do Simples Nacional - Contador. Trib. aprox. R$ 53,80 Federal e R$ 20,00 Municipal. Fonte: IBPT [A906AF]. Alíquota do Simples Nacional: 2,0000%
```

Nesse cenário nada mais muda: os R$ 8,00 a 2% estão corretos e no piso legal (art. 8º-A da LC 116/2003).

---

Resumindo a lógica: os campos estruturais do documento descrevem um contador **percentual** (Cenário B pronto para valer), enquanto o texto livre anuncia um contador **fixo**. Um dos dois está mentindo. Se você me disser se Aracaju tem ISS fixo para contadores e se a empresa é uniprofissional ou empresária, eu te digo com certeza qual dos dois trechos aplicar — e, no Cenário A, se você me passar o valor fixo da lei de Aracaju, eu completo o `vISSQN` e recalculo o `vLiq`.
