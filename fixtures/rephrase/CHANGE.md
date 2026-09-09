# CHANGE — rephrase/ (the same violation, the surrounding text reworded three ways)

- **Base:** `fixtures/mutations/m1-codigo-servico/nfse.xml` — the wrong service code (`cTribNac` = 010101, systems analysis, on a note of an accounting client whose profile says item 17.19). The code is **not** changed here.
- **Field changed (one, three ways):** `xDescServ`, the free-text description of the service, rewritten in `m1-rephrase-a.xml`, `-b.xml` and `-c.xml`:
  - a: "Honorários contábeis referentes ao mês de agosto de 2026."
  - b: "Prestação de serviços de contabilidade - competência 08/2026. Trib aprox R$: 53,80 Federal, R$: 0,00 Estadual e R$: 20,00 Municipal Fonte: IBPT"
  - c: "Assessoria contábil mensal conforme contrato. Valor R$ 400,00."
- **Check that must catch it, three times:** check 1 — rule: LC116 list item 17 · LC116 art. 1. The `1-código` row must FAIL on each of the three, because the code on the note does not match the profile's item, whatever the description says. The `1-descrição` row stays CANNOT DETERMINE on each (description × code is judgement).
- **Why this exists:** an auditor that fires on one wording and not on the others is reading the phrasing, not the provision. Each file is fed in a **separate** conversation, so that no answer can copy the previous one.
- **What it is:** a synthetic bench test written by the author, declared as such. It proves the mechanism on the author's own note; the real test is the round in which the office's assistant feeds notes she chose.
- **Expected:** `expected/m1-rephrase-a.md`, `-b.md`, `-c.md`.
