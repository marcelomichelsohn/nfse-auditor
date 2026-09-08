#!/usr/bin/env python3
"""anonymise.py — the single path from a real NFS-e XML to a fixture. Standard library only. Runs on the author's machine;
the raw files and the mapping never enter this repository.

    python3 tools/anonymise.py <raw-dir-or-file> <out-dir> --map <mapping.json> [--review <REVIEW.md>]

What it does, by class (single source of this list: fixtures/README.md):
- identity numbers  CNPJ, CPF, IM, nNFSe, nDPS, nDFSe, cIntContrib, the Id attributes  -> synthetic values of the same
                    format (CNPJ/CPF with valid check digits), consistent across files through the mapping; files renamed nfse-NN.xml
- people/companies  xNome, xFant, address lines (xLgr, nro, xCpl, xBairro)  -> placeholders (PRESTADOR CONTABIL LTDA, TOMADOR NN LTDA, ...)
- free text         xDescServ, xOutInf  -> kept in structure; every occurrence of a mapped name/number replaced; the before/after is
                    printed to the review file for a human decision, line by line
- contacts          fone, email -> fixed fakes; CEP keeps its first 5 digits + 000
- kept              municipality codes (cMun, cLocEmi, cLocPrestacao, cLocIncid, UF), dates, values, tax flags, cTribNac, verAplic, ambGer, cStat
- stripped          the whole <Signature> block (certificate = real name + CNPJ; digests bind to the real content)
"""
import os, sys, re, json, glob, hashlib, xml.etree.ElementTree as ET

NS = "http://www.sped.fazenda.gov.br/nfse"
ET.register_namespace("", NS)
DS = "http://www.w3.org/2000/09/xmldsig#"

def cnpj_dv(base12):
    def dv(nums, w): s = sum(int(n)*k for n, k in zip(nums, w)); r = s % 11; return "0" if r < 2 else str(11 - r)
    w1 = [5,4,3,2,9,8,7,6,5,4,3,2]; w2 = [6] + w1
    d1 = dv(base12, w1); return base12 + d1 + dv(base12 + d1, w2)
def cpf_dv(base9):
    def dv(nums, start): s = sum(int(n)*k for n, k in zip(nums, range(start, 1, -1))); r = (s*10) % 11; return "0" if r == 10 else str(r)
    d1 = dv(base9, 10); return base9 + d1 + dv(base9 + d1, 11)

class Mapper:
    def __init__(self, path):
        self.path = path; self.m = json.load(open(path)) if os.path.exists(path) else {"cnpj": {}, "cpf": {}, "im": {}, "name": {}, "num": {}, "file": {}, "counter": {}}
    def save(self): json.dump(self.m, open(self.path, "w"), indent=1, ensure_ascii=False)
    def nxt(self, k): self.m["counter"][k] = self.m["counter"].get(k, 0) + 1; return self.m["counter"][k]
    def cnpj(self, real):
        if real not in self.m["cnpj"]:
            n = self.nxt("cnpj"); self.m["cnpj"][real] = cnpj_dv(f"{99000000:08d}{n:04d}")
        return self.m["cnpj"][real]
    def cpf(self, real):
        if real not in self.m["cpf"]: n = self.nxt("cpf"); self.m["cpf"][real] = cpf_dv(f"{990000000 + n:09d}")
        return self.m["cpf"][real]
    def name(self, real, role):
        if real not in self.m["name"]:
            n = self.nxt("name_" + role); self.m["name"][real] = f"{role} {n:02d} LTDA" if role != "PRESTADOR" else "PRESTADOR CONTABIL LTDA"
        return self.m["name"][real]
    def num(self, real, width):
        if real not in self.m["num"]: n = self.nxt("num"); self.m["num"][real] = str(n).rjust(width, "0")[-width:]
        return self.m["num"][real]
    def file(self, real):
        if real not in self.m["file"]: n = self.nxt("file"); self.m["file"][real] = f"nfse-{n:02d}.xml"
        return self.m["file"][real]

def q(tag): return f"{{{NS}}}{tag}"

def anonymise_file(path, out_dir, mp, review):
    tree = ET.parse(path); root = tree.getroot()
    # strip signature
    for sig in list(root):
        if sig.tag == f"{{{DS}}}Signature": root.remove(sig)
    reps = {}  # real -> fake, for free-text sweeps
    for el in root.iter():
        tag = re.sub(r"\{.*\}", "", el.tag); txt = (el.text or "").strip()
        if not txt and not el.attrib: continue
        if tag == "CNPJ": fake = mp.cnpj(txt); reps[txt] = fake; el.text = fake
        elif tag == "CPF": fake = mp.cpf(txt); reps[txt] = fake; el.text = fake
        elif tag in ("IM", "nDFSe"): fake = mp.num(txt, len(txt)); reps[txt] = fake; el.text = fake
        elif tag in ("nNFSe", "nDPS"): fake = mp.num(txt, len(txt)); reps[txt] = fake; el.text = fake
        elif tag == "cIntContrib": fake = "FIX" + mp.num(txt, 6); reps[txt] = fake; el.text = fake
        elif tag in ("xNome", "xFant"):
            role = "PRESTADOR" if _under(root, el, ("emit", "prest")) else "TOMADOR"
            fake = mp.name(txt, role); reps[txt] = fake; el.text = fake
        elif tag in ("xLgr",): el.text = "RUA EXEMPLO"
        elif tag == "nro": el.text = "100"
        elif tag == "xCpl": el.text = "SALA 1"
        elif tag == "xBairro": el.text = "CENTRO"
        elif tag == "fone": el.text = "0000000000"
        elif tag == "email": el.text = "exemplo@exemplo.invalid"
        elif tag == "CEP": el.text = txt[:5] + "000"
    # Id attributes and free text
    for el in root.iter():
        tag = re.sub(r"\{.*\}", "", el.tag)
        if "Id" in el.attrib:
            v = el.attrib["Id"]; h = hashlib.sha256(v.encode()).hexdigest()[:8].upper()
            el.attrib["Id"] = re.sub(r"\d{6,}", lambda m: (h * 8)[:len(m.group(0))], v)
        if tag in ("xDescServ", "xOutInf") and el.text:
            before = el.text; after = before
            for real, fake in sorted(reps.items(), key=lambda kv: -len(kv[0])): after = after.replace(real, fake)
            for real, fake in mp.m["name"].items():
                for piece in [w for w in re.split(r"\s+", real) if len(w) >= 4]: after = re.sub(re.escape(piece), fake.split()[0], after, flags=re.I)
            el.text = after
            review.append(f"### {os.path.basename(path)} → `{tag}`\n- before: {before}\n- after:  {after}\n")
    out_name = mp.file(os.path.basename(path)); out = os.path.join(out_dir, out_name)
    tree.write(out, encoding="utf-8", xml_declaration=True)
    return out_name

def _under(root, el, parents):
    for p in root.iter():
        if el in list(p) and re.sub(r"\{.*\}", "", p.tag) in parents: return True
    return False

def main():
    args = sys.argv[1:]
    if len(args) < 3 or "--map" not in args: print(__doc__); sys.exit(2)
    src, out_dir = args[0], args[1]; mp = Mapper(args[args.index("--map") + 1])
    rev_path = args[args.index("--review") + 1] if "--review" in args else os.path.join(out_dir, "REVIEW.md")
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src, "*.xml"))) if os.path.isdir(src) else [src]
    review = ["# REVIEW — free-text fields before → after, and what was kept (for the author's per-file decision)\n"]
    for f in files:
        name = anonymise_file(f, out_dir, mp, review); print(f"{os.path.basename(f)} -> {name}")
    review.append("\nKept as-is in every file: municipality codes, dates, values, tax flags, cTribNac, verAplic, ambGer, cStat. Stripped: Signature block.\n")
    open(rev_path, "w").write("\n".join(review)); mp.save()
    print("review:", rev_path)

if __name__ == "__main__": main()
