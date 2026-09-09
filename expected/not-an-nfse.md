# expected — not-an-nfse.txt (a file that is not a national-standard NFS-e XML)

**What was fed:** `fixtures/unreadable/not-an-nfse.txt` + the profile line `perfil: CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não`.
**This file is outside the folder the operator loads.**

A correct answer has **no report rows** for this file and no totals line for it (no `vServ` was read). It ends with the file listed under `Não lidos:` with the reason — not XML, not the national NFS-e layout (`rules.md` § 0 and § 3). No field may be inferred from the text.

Totais para a sua comparação: — (nothing read)

Não lidos: not-an-nfse.txt — não é XML de NFS-e no padrão nacional (texto simples).
