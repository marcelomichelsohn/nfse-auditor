# EVIDENCE, NOT A TOOL OF THIS FOLDER. Written by the bare model (Claude Fable 5.1, web on) in run B3 of
# rounds/control-bare-model/ on 2026-09-09, when the operator typed "continue" after its review — see transcript-B3.md.
# Kept exactly as it came out of that conversation, so a reader can see what "no folder" produced. It is not loaded
# with the auditor, it is not run by check_audit.py or prove_order.py, and its verdicts are the bare model's own.

#!/usr/bin/env python3
"""
nfse_check.py — confere uma NFS-e (leiaute nacional v1.0x) contra o cadastro do cliente
(linha "perfil"), a LC 116/2003, as regras do Simples Nacional e o leiaute da NFS-e.

Uso:
    python3 nfse_check.py nota.xml "CNAE 6920-6/01; regime Simples optante; anexo fixo; município 2800308; item LC 116 17.19; exporta não"
    python3 nfse_check.py nota.xml --perfil perfil.txt
    python3 nfse_check.py nota.xml "..." --json

Cada achado traz: resultado (PASSA / FALHA / AVISO), risco (alto/médio/baixo),
confiança (alta/média/baixa), onde (caminho no XML), norma e correção sugerida.
"""
import argparse
import json
import re
import sys
from datetime import date, datetime
from decimal import Decimal
from xml.etree import ElementTree as ET

NS = {"n": "http://www.sped.fazenda.gov.br/nfse"}

# --- Tabelas do leiaute (Manual de Integração v1.01 / regras de negócio) --------------------------

# Códigos cuja incidência é o local da prestação (LC 116, art. 3º, exceções, refletidas no leiaute)
INCID_LOCAL_PRESTACAO = set("""
030401 030402 030403 030501 070201 070202 070401 070501 070502 070901 070902 071001 071002 071101
071102 071201 071601 071701 071801 071901 110101 110102 110201 110401 110402 120101 120201 120301
120401 120501 120601 120701 120801 120901 120902 120903 121001 121101 121201 121401 121501 121601
121701 141401 141402 141403 141404 160101 160102 160103 160104 160201 171001 171002 200101 200102
200201 200301 220101
""".split())
INCID_TOMADOR = {"170501"}
INCID_LIVRE = {"990101"}

# Códigos dispensados do piso de 2% de alíquota efetiva (LC 116, art. 8º-A, § 1º, refletido no leiaute)
DISPENSA_PISO_2 = set("""
042201 042301 050901 070201 070202 070501 070502 090201 090202 100101 100102 100103 100104 100105
100201 100202 100301 100401 100402 100403 100501 100502 100601 100701 100801 100901 101001 150101
150102 150103 150104 150105 151001 151002 151003 151004 151005 160101 160102 160103 160104 160201
170501 170601 171001 171002 171101 171102 171201 210101 250301
""".split())

# CNAE -> itens LC 116 esperados (amplie conforme a carteira de clientes)
CNAE_ITENS = {
    "6920-6/01": {"17.19"},            # atividades de contabilidade
    "6920-6/02": {"17.19", "17.20"},   # consultoria e auditoria contábil e tributária
    "6911-7/01": {"17.14"},            # advocacia
    "8630-5/03": {"4.01"},             # atividade médica ambulatorial restrita a consultas
    "8650-0/03": {"4.16"},             # psicologia e psicanálise
    "6201-5/01": {"1.01", "1.02", "1.04", "1.05"},
}

# Obrigatoriedade do Emissor Nacional para ME/EPP (Res. CGSN 191/2026, que revogou a 189/2026)
DATA_EMISSOR_NACIONAL_OBRIG = date(2026, 11, 1)
# Grupo IBS/CBS obrigatório para competência posterior a esta data (NT 009, conforme manual v1.01 rev. 03/08/2026)
DATA_IBSCBS_OBRIG = date(2026, 10, 1)


# --- utilidades --------------------------------------------------------------------------------

def txt(node, path):
    el = node.find(path, NS) if node is not None else None
    return el.text.strip() if el is not None and el.text else None


def dec(v):
    return Decimal(v) if v not in (None, "") else None


def cnpj_valido(c):
    if not c or not re.fullmatch(r"\d{14}", c):
        return False
    def dv(nums, w):
        s = sum(int(n) * x for n, x in zip(nums, w))
        r = s % 11
        return "0" if r < 2 else str(11 - r)
    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    d1 = dv(c[:12], w1)
    d2 = dv(c[:12] + d1, [6] + w1)
    return c[12:] == d1 + d2


def cpf_valido(c):
    if not c or not re.fullmatch(r"\d{11}", c) or c == c[0] * 11:
        return False
    for k in (9, 10):
        s = sum(int(c[i]) * (k + 1 - i) for i in range(k))
        r = (s * 10) % 11 % 10
        if r != int(c[k]):
            return False
    return True


def item_to_ctrib(item):
    """'17.19' -> '1719' (prefixo do cTribNac de 6 dígitos)."""
    a, b = item.split(".")
    return f"{int(a):02d}{int(b):02d}"


def parse_perfil(s):
    p = {}
    for part in [x.strip() for x in s.split(";") if x.strip()]:
        low = part.lower()
        if low.startswith("cnae"):
            p["cnae"] = part.split(None, 1)[1].strip()
        elif low.startswith("regime"):
            p["regime"] = part.split(None, 1)[1].strip().lower()
        elif low.startswith("anexo"):
            p["anexo"] = part.split(None, 1)[1].strip().lower()
        elif low.startswith("munic"):
            p["municipio"] = re.sub(r"\D", "", part)
        elif low.startswith("item"):
            p["item"] = re.search(r"(\d{1,2}\.\d{1,2})", part).group(1)
        elif low.startswith("exporta"):
            p["exporta"] = part.split(None, 1)[1].strip().lower()
    return p


class Report:
    def __init__(self):
        self.itens = []

    def add(self, cod, resultado, msg, onde, norma, risco=None, conf="alta", correcao=None):
        self.itens.append(dict(codigo=cod, resultado=resultado, mensagem=msg, onde=onde,
                               norma=norma, risco=risco, confianca=conf, correcao=correcao))

    passa = lambda self, *a, **k: self.add(*a[:1], "PASSA", *a[1:], **k)
    falha = lambda self, *a, **k: self.add(*a[:1], "FALHA", *a[1:], **k)
    aviso = lambda self, *a, **k: self.add(*a[:1], "AVISO", *a[1:], **k)


# --- extração ---------------------------------------------------------------------------------

def extrair(root):
    inf = root.find("n:infNFSe", NS)
    dps = inf.find("n:DPS/n:infDPS", NS)
    emit = inf.find("n:emit", NS)
    prest = dps.find("n:prest", NS)
    toma = dps.find("n:toma", NS)
    d = dict(
        inf=inf, dps=dps,
        id_nfse=inf.get("Id"), id_dps=dps.get("Id"),
        versao=root.get("versao"),
        nNFSe=txt(inf, "n:nNFSe"), nDFSe=txt(inf, "n:nDFSe"),
        cLocIncid=txt(inf, "n:cLocIncid"), xTribNac=txt(inf, "n:xTribNac"),
        ambGer=txt(inf, "n:ambGer"), tpEmis=txt(inf, "n:tpEmis"), cStat=txt(inf, "n:cStat"),
        dhProc=txt(inf, "n:dhProc"), verAplic=txt(inf, "n:verAplic"),
        emit_cnpj=txt(emit, "n:CNPJ"), emit_cpf=txt(emit, "n:CPF"),
        emit_cMun=txt(emit, "n:enderNac/n:cMun"),
        vCalcDR=dec(txt(inf, "n:valores/n:vCalcDR")), vBC=dec(txt(inf, "n:valores/n:vBC")),
        pAliqAplic=dec(txt(inf, "n:valores/n:pAliqAplic")), vISSQN=dec(txt(inf, "n:valores/n:vISSQN")),
        vTotalRet=dec(txt(inf, "n:valores/n:vTotalRet")), vLiq=dec(txt(inf, "n:valores/n:vLiq")),
        xOutInf=txt(inf, "n:xOutInf") or "",
        tpAmb=txt(dps, "n:tpAmb"), dhEmi=txt(dps, "n:dhEmi"), serie=txt(dps, "n:serie"),
        nDPS=txt(dps, "n:nDPS"), dCompet=txt(dps, "n:dCompet"), tpEmit=txt(dps, "n:tpEmit"),
        cLocEmi=txt(dps, "n:cLocEmi"),
        prest_cnpj=txt(prest, "n:CNPJ"), prest_cpf=txt(prest, "n:CPF"),
        opSimpNac=txt(prest, "n:regTrib/n:opSimpNac"),
        regApTribSN=txt(prest, "n:regTrib/n:regApTribSN"),
        regEspTrib=txt(prest, "n:regTrib/n:regEspTrib"),
        toma=toma, toma_cnpj=txt(toma, "n:CNPJ"), toma_cpf=txt(toma, "n:CPF"),
        toma_nif=txt(toma, "n:NIF"), toma_cNaoNIF=txt(toma, "n:cNaoNIF"),
        toma_cMun=txt(toma, "n:end/n:endNac/n:cMun"), toma_ext=toma.find("n:end/n:endExt", NS) is not None if toma is not None else False,
        cLocPrestacao=txt(dps, "n:serv/n:locPrest/n:cLocPrestacao"),
        cPaisPrestacao=txt(dps, "n:serv/n:locPrest/n:cPaisPrestacao"),
        cTribNac=txt(dps, "n:serv/n:cServ/n:cTribNac"), cTribMun=txt(dps, "n:serv/n:cServ/n:cTribMun"),
        xDescServ=txt(dps, "n:serv/n:cServ/n:xDescServ") or "",
        comExt=dps.find("n:serv/n:comExt", NS) is not None,
        vServ=dec(txt(dps, "n:valores/n:vServPrest/n:vServ")),
        vDescIncond=dec(txt(dps, "n:valores/n:vDescCondIncond/n:vDescIncond")),
        vDescCond=dec(txt(dps, "n:valores/n:vDescCondIncond/n:vDescCond")),
        tribISSQN=txt(dps, "n:valores/n:trib/n:tribMun/n:tribISSQN"),
        tpRetISSQN=txt(dps, "n:valores/n:trib/n:tribMun/n:tpRetISSQN"),
        pAliq=dec(txt(dps, "n:valores/n:trib/n:tribMun/n:pAliq")),
        exigSusp=dps.find("n:valores/n:trib/n:tribMun/n:exigSusp", NS) is not None,
        totTrib=dps.find("n:valores/n:trib/n:totTrib", NS),
        vTotTribMun=dec(txt(dps, "n:valores/n:trib/n:totTrib/n:vTotTrib/n:vTotTribMun")),
        vTotTribFed=dec(txt(dps, "n:valores/n:trib/n:totTrib/n:vTotTrib/n:vTotTribFed")),
        ibscbs=dps.find("n:IBSCBS", NS) is not None,
        signature=root.find(".//{http://www.w3.org/2000/09/xmldsig#}Signature") is not None,
    )
    return d


# --- regras -----------------------------------------------------------------------------------

def checar(d, p, r):
    ctrib = d["cTribNac"] or ""
    simples = "simples" in p.get("regime", "") and "não" not in p.get("regime", "")
    mei = "mei" in p.get("regime", "")
    fixo = "fixo" in p.get("anexo", "")
    exporta = p.get("exporta", "").startswith("s")
    try:
        d_emi = datetime.fromisoformat(d["dhEmi"]).date() if d["dhEmi"] else None
        d_comp = date.fromisoformat(d["dCompet"]) if d["dCompet"] else None
        d_proc = datetime.fromisoformat(d["dhProc"]).date() if d["dhProc"] else None
    except ValueError:
        d_emi = d_comp = d_proc = None
        r.falha("DAT-00", "Data em formato inválido", "dhEmi/dCompet/dhProc", "Leiaute (TSDateTimeUTC / TSData)", "médio")

    # R01 — serviço x perfil
    onde = "DPS/infDPS/serv/cServ/cTribNac"
    if p.get("item"):
        esperado = item_to_ctrib(p["item"])
        if ctrib.startswith(esperado):
            r.passa("SRV-01", f"cTribNac {ctrib} corresponde ao item {p['item']} do perfil", onde,
                    f"LC 116/2003, lista anexa, item {p['item']}")
        else:
            r.falha("SRV-01", f"cTribNac {ctrib} não corresponde ao item {p['item']} do perfil", onde,
                    f"LC 116/2003, lista anexa, item {p['item']}", "alto",
                    correcao=f"usar código iniciado por {esperado} ou corrigir o perfil")
    if p.get("cnae") and p["cnae"] in CNAE_ITENS:
        if any(ctrib.startswith(item_to_ctrib(i)) for i in CNAE_ITENS[p["cnae"]]):
            r.passa("SRV-02", f"CNAE {p['cnae']} compatível com o item faturado", onde, "Lista LC 116 x CNAE (tabela local)")
        else:
            r.aviso("SRV-02", f"CNAE {p['cnae']} normalmente fatura {sorted(CNAE_ITENS[p['cnae']])}, nota traz {ctrib}",
                    onde, "Lista LC 116 x CNAE (tabela local)", "médio", "média")
    elif p.get("cnae"):
        r.aviso("SRV-02", f"CNAE {p['cnae']} sem mapeamento na tabela local — conferir manualmente", onde,
                "—", "baixo", "baixa")

    # R02 — local de incidência
    onde = "infNFSe/cLocIncid"
    if d["tribISSQN"] == "1" and not d["exigSusp"] and d["regEspTrib"] in (None, "0"):
        if ctrib in INCID_TOMADOR:
            esperado, base = d["toma_cMun"], "LC 116, art. 3º, XXIII (17.05) — município do tomador"
        elif ctrib in INCID_LOCAL_PRESTACAO:
            esperado, base = d["cLocPrestacao"], "LC 116, art. 3º, incisos I a XXV — local da prestação"
        elif ctrib in INCID_LIVRE:
            esperado, base = None, "código 99.01.01 — sem regra automática"
        else:
            esperado, base = d["emit_cMun"], "LC 116, art. 3º, caput — estabelecimento prestador"
        if esperado is None:
            r.aviso("LOC-01", "Local de incidência não verificável automaticamente", onde, base, "médio", "média")
        elif d["cLocIncid"] == esperado:
            r.passa("LOC-01", f"cLocIncid {d['cLocIncid']} correto para o código {ctrib}", onde, base)
        else:
            r.falha("LOC-01", f"cLocIncid {d['cLocIncid']} diverge do esperado {esperado}", onde, base, "alto",
                    correcao=f"cLocIncid = {esperado}")
        if p.get("municipio") and d["cLocIncid"] != p["municipio"] and esperado == d["emit_cMun"]:
            r.falha("LOC-02", f"Município de incidência {d['cLocIncid']} ≠ município do perfil {p['municipio']}",
                    onde, "Cadastro do cliente x LC 116, art. 3º", "alto")
    else:
        r.aviso("LOC-01", "Incidência não avaliada (imunidade/exportação/não incidência/exigibilidade suspensa/regime especial)",
                onde, "Leiaute: cLocIncid não é informado nesses casos", "baixo")
    if p.get("municipio") and d["emit_cMun"] and d["emit_cMun"] != p["municipio"]:
        r.falha("LOC-03", f"Endereço do emitente ({d['emit_cMun']}) não é o município do perfil ({p['municipio']})",
                "infNFSe/emit/enderNac/cMun", "Cadastro do cliente", "alto")

    # R03 — retenção
    onde = "DPS/infDPS/valores/trib/tribMun/tpRetISSQN"
    if d["tpRetISSQN"] == "1":
        r.passa("RET-01", "ISS não retido", onde, "LC 116, art. 6º, § 2º; LC 123, art. 21, § 4º")
    elif d["tpRetISSQN"] in ("2", "3"):
        if ctrib not in INCID_LOCAL_PRESTACAO and ctrib not in INCID_TOMADOR:
            r.aviso("RET-01", "Retenção declarada em serviço fora das hipóteses do art. 3º — só vale se a lei do município de incidência atribuir responsabilidade",
                    onde, "LC 116, art. 6º, § 2º; LC 123, art. 21, § 4º", "médio", "média",
                    "confirmar responsabilidade tributária na legislação de " + str(d["cLocIncid"]))
        elif d["toma_cMun"] and d["cLocIncid"] and d["toma_cMun"] != d["cLocIncid"] and d["tpRetISSQN"] == "2":
            r.aviso("RET-02", "Tomador em município diferente do de incidência retendo ISS", onde,
                    "LC 116, art. 6º", "médio", "média")
        else:
            r.passa("RET-01", "Retenção compatível com a hipótese de incidência", onde, "LC 116, art. 6º, § 2º")

    # R04 — base, alíquota, líquido
    if d["vServ"] is not None:
        base_esp = d["vServ"] - (d["vDescIncond"] or 0) - (d["vCalcDR"] or 0)
        if d["vBC"] == base_esp:
            r.passa("VAL-01", f"vBC {d['vBC']} = preço do serviço − deduções/desconto incondicionado", "infNFSe/valores/vBC",
                    "LC 116, art. 7º; leiaute (base = vServ − deduções − desc. incond.)")
        else:
            r.falha("VAL-01", f"vBC {d['vBC']} ≠ esperado {base_esp}", "infNFSe/valores/vBC", "LC 116, art. 7º", "alto")
    if d["vISSQN"] is not None and d["vBC"] and d["vBC"] > 0 and d["tribISSQN"] == "1":
        efet = (d["vISSQN"] / d["vBC"] * 100).quantize(Decimal("0.0001"))
        if d["pAliqAplic"] is not None and (d["vBC"] * d["pAliqAplic"] / 100).quantize(Decimal("0.01")) != d["vISSQN"]:
            r.falha("VAL-02", f"vISSQN {d['vISSQN']} ≠ vBC × pAliqAplic", "infNFSe/valores/vISSQN", "Leiaute: vISSQN = vBC × alíquota", "alto")
        if d["vISSQN"] > 0:
            if efet < 2 and ctrib not in DISPENSA_PISO_2:
                r.falha("VAL-03", f"Alíquota efetiva {efet}% abaixo do piso de 2%", "infNFSe/valores", "LC 116, art. 8º-A; ADCT, art. 88", "alto")
            elif efet > 5:
                r.falha("VAL-03", f"Alíquota efetiva {efet}% acima do teto de 5%", "infNFSe/valores", "LC 116, art. 8º, II", "alto")
            else:
                r.passa("VAL-03", f"Alíquota efetiva {efet}% dentro de [2%, 5%]", "infNFSe/valores", "LC 116, art. 8º, II e 8º-A")
        if d["pAliqAplic"] is None and d["vISSQN"] > 0:
            r.aviso("VAL-04", "pAliqAplic ausente embora vISSQN tenha sido calculado", "infNFSe/valores/pAliqAplic",
                    "Leiaute NFS-e (grupo valores)", "baixo", "média")
    if d["vLiq"] is not None and d["vServ"] is not None:
        ret = d["vTotalRet"] or 0
        liq_esp = d["vServ"] - (d["vDescIncond"] or 0) - (d["vDescCond"] or 0) - ret
        if d["vLiq"] == liq_esp:
            r.passa("VAL-05", f"vLiq {d['vLiq']} coerente", "infNFSe/valores/vLiq", "Leiaute: líquido = vServ − descontos − retenções")
        else:
            r.falha("VAL-05", f"vLiq {d['vLiq']} ≠ esperado {liq_esp}", "infNFSe/valores/vLiq", "Leiaute: líquido = vServ − descontos − retenções", "médio")
    if d["pAliq"] is not None and d["tpRetISSQN"] == "1" and d["cLocIncid"] == d["emit_cMun"]:
        r.aviso("VAL-06", "pAliq informado pelo contribuinte fora das hipóteses (fora do município ou SN com retenção)",
                "DPS/.../tribMun/pAliq", "Leiaute: alíquota é definida pela legislação municipal", "médio", "média")

    # R05 — situação no Simples
    onde = "DPS/infDPS/prest/regTrib/opSimpNac"
    esperado = "2" if mei else "3" if simples else "1"
    if d["opSimpNac"] == esperado:
        r.passa("SN-01", f"opSimpNac {d['opSimpNac']} coerente com o regime do perfil", onde, "LC 123/2006; leiaute TSOpSimpNac")
    else:
        r.falha("SN-01", f"opSimpNac {d['opSimpNac']} ≠ esperado {esperado} para '{p.get('regime')}'", onde,
                "LC 123/2006; leiaute TSOpSimpNac", "alto", correcao=f"opSimpNac = {esperado} ou corrigir o perfil")
    if d["cStat"] == "107" and not mei:
        r.falha("SN-02", "cStat 107 (NFS-e MEI) para prestador não-MEI", "infNFSe/cStat", "Leiaute TStat", "médio")
    if d["opSimpNac"] == "3" and not d["regApTribSN"]:
        r.falha("SN-03", "regApTribSN obrigatório para optante ME/EPP", "DPS/.../regTrib/regApTribSN", "Leiaute (rejeição E0166)", "alto")

    # R06 — ISS fixo (escritórios contábeis) x regime de apuração
    onde = "DPS/infDPS/prest/regTrib/regApTribSN"
    if simples and not mei:
        if fixo:
            norma = "LC 123, art. 18, § 22-A; Res. CGSN 140/2018, art. 25"
            if d["regApTribSN"] == "1":
                r.falha("SN-04", "Perfil diz ISS fixo, mas a nota declara ISS apurado dentro do Simples (regApTribSN = 1)",
                        onde, norma, "alto", correcao="regApTribSN = 2 (federais pelo SN, ISS conforme legislação municipal)")
            else:
                r.passa("SN-04", f"regApTribSN {d['regApTribSN']} compatível com ISS fora do DAS", onde, norma)
            if d["regEspTrib"] in (None, "0"):
                r.falha("SN-05", "ISS fixo sem regime especial declarado (regEspTrib = 0): o ADN calcula ISS ad valorem",
                        "DPS/.../regTrib/regEspTrib", "Leiaute: ISSQN não é calculado quando há regime especial; " + norma,
                        "alto", "média", correcao="informar o regEspTrib parametrizado pelo município (ex.: 6 – Sociedade de Profissionais)")
            if d["vISSQN"] and d["vISSQN"] > 0:
                r.falha("SN-06", f"vISSQN {d['vISSQN']} destacado em nota de contribuinte com ISS fixo", "infNFSe/valores/vISSQN",
                        norma, "alto", correcao="ISS fixo é pago em guia própria, independente do faturamento; nota deve sair sem ISS calculado")
            if re.search(r"al[ií]quota do simples", d["xOutInf"], re.I):
                r.aviso("SN-07", "xOutInf rotula um percentual como 'alíquota do Simples Nacional' — impreciso para ISS fixo",
                        "infNFSe/xOutInf", "LC 123, art. 18", "médio", "alta", correcao="remover ou substituir pela informação do regime fixo")
        else:
            if d["regApTribSN"] == "1":
                r.passa("SN-04", "ISS apurado dentro do Simples (regApTribSN = 1)", onde, "LC 123, art. 13, VIII; art. 18")
            elif d["regApTribSN"] in ("2", "3"):
                r.aviso("SN-04", f"regApTribSN {d['regApTribSN']}: ISS fora do DAS — só cabe se houve sublimite estourado ou ISS fixo autorizado",
                        onde, "LC 123, art. 19/20 (sublimite); art. 18, § 22-A", "médio", "média")

    # R07 — exportação
    onde = "DPS/infDPS/valores/trib/tribMun/tribISSQN"
    if exporta:
        if d["tribISSQN"] == "3" and d["comExt"]:
            r.passa("EXP-01", "Exportação declarada com grupo comExt", onde, "LC 116, art. 2º, I e parágrafo único")
        else:
            r.falha("EXP-01", "Perfil exporta, mas a nota não traz tribISSQN = 3 e/ou o grupo comExt", onde,
                    "LC 116, art. 2º, I; leiaute (comExt obrigatório na exportação)", "médio", "média")
    else:
        if d["tribISSQN"] == "3" or d["comExt"] or d["toma_ext"] or d["cPaisPrestacao"]:
            r.falha("EXP-01", "Nota com traços de exportação, perfil diz que não exporta", onde, "LC 116, art. 2º, I", "alto")
        else:
            r.passa("EXP-01", "Operação interna, sem grupo comExt", onde, "LC 116, art. 2º, I (não aplicável)")

    # R08 — datas
    if d_emi and d_comp:
        if d_comp <= d_emi:
            r.passa("DAT-01", f"dCompet {d_comp} ≤ dhEmi {d_emi}", "DPS/infDPS/dCompet", "LC 116, art. 1º (fato gerador); leiaute")
        else:
            r.falha("DAT-01", "Competência posterior à emissão", "DPS/infDPS/dCompet", "LC 116, art. 1º", "médio")
    if d_emi and d_proc and d_proc < d_emi:
        r.falha("DAT-02", "dhProc anterior a dhEmi", "infNFSe/dhProc", "Leiaute", "médio")

    # R09 — canal de emissão (Simples x Emissor Nacional)
    if d["opSimpNac"] == "3" and d["tpEmis"] == "2" and d_emi:
        onde = "infNFSe/tpEmis + ambGer + verAplic"
        norma = "Res. CGSN 140/2018, art. 59, § 1º (red. Res. 189/2026, adiada p/ 1º/11/2026 pela Res. 191/2026)"
        if d_emi >= DATA_EMISSOR_NACIONAL_OBRIG:
            r.falha("EMI-01", "ME/EPP emitindo por sistema municipal após a obrigatoriedade do Emissor Nacional", onde, norma, "alto")
        else:
            r.aviso("EMI-01", f"Emitida por sistema municipal (transcrita); a partir de {DATA_EMISSOR_NACIONAL_OBRIG:%d/%m/%Y} só vale o Emissor Nacional",
                    onde, norma, "baixo")

    # R10 — identificadores
    onde = "infNFSe/@Id"
    if d["id_nfse"] and re.fullmatch(r"NFS\d{50}", d["id_nfse"]):
        insc = d["emit_cnpj"] or (d["emit_cpf"] or "").rjust(14, "0")
        tipo = "2" if d["emit_cnpj"] else "1"
        pref = f"NFS{d['emit_cMun']}{d['ambGer']}{tipo}{insc}{(d['nNFSe'] or '').rjust(13, '0')}"
        if d["id_nfse"].startswith(pref):
            r.passa("ID-01", "Id da NFS-e no formato e coerente com emitente/número", onde, "Leiaute TSIdNFSe")
        else:
            r.falha("ID-01", f"Id da NFS-e numérico, mas não bate com os campos (esperado prefixo {pref})", onde, "Leiaute TSIdNFSe", "alto", "média")
    else:
        r.falha("ID-01", "Id da NFS-e fora do formato 'NFS' + 50 dígitos (cMun7+ambGer1+tipoInsc1+insc14+nNFSe13+AAMM4+cod9+DV1)",
                onde, "Leiaute TSIdNFSe (XSD)", "alto")
    onde = "DPS/infDPS/@Id"
    if d["id_dps"] and re.fullmatch(r"DPS\d{42}", d["id_dps"]):
        insc = d["prest_cnpj"] or (d["prest_cpf"] or "").rjust(14, "0")
        tipo = "2" if d["prest_cnpj"] else "1"
        esp = f"DPS{d['cLocEmi']}{tipo}{insc}{(d['serie'] or '').rjust(5, '0')}{(d['nDPS'] or '').rjust(15, '0')}"
        if d["id_dps"] == esp:
            r.passa("ID-02", "Id da DPS coerente com município/inscrição/série/número", onde, "Leiaute TSIdDPS")
        else:
            r.falha("ID-02", f"Id da DPS numérico, mas ≠ esperado {esp}", onde, "Leiaute TSIdDPS", "alto", "média")
    else:
        r.falha("ID-02", "Id da DPS fora do formato 'DPS' + 42 dígitos (cMun7+tipoInsc1+insc14+serie5+nDPS15)", onde, "Leiaute TSIdDPS (XSD)", "alto")

    # R11 — documentos
    for rot, cnpj, cpf, onde in (("emitente", d["emit_cnpj"], d["emit_cpf"], "infNFSe/emit"),
                                 ("prestador", d["prest_cnpj"], d["prest_cpf"], "DPS/infDPS/prest"),
                                 ("tomador", d["toma_cnpj"], d["toma_cpf"], "DPS/infDPS/toma")):
        if cnpj is not None:
            (r.passa if cnpj_valido(cnpj) else lambda *a, **k: r.falha(*a, "alto", **k))("DOC-" + rot[:3].upper(), f"CNPJ do {rot} {'válido' if cnpj_valido(cnpj) else 'com DV inválido'}", onde + "/CNPJ", "Validação de dígitos (rejeição do ADN)")
        elif cpf is not None:
            (r.passa if cpf_valido(cpf) else lambda *a, **k: r.falha(*a, "alto", **k))("DOC-" + rot[:3].upper(), f"CPF do {rot} {'válido' if cpf_valido(cpf) else 'com DV inválido'}", onde + "/CPF", "Validação de dígitos (rejeição do ADN)")
    if d["emit_cnpj"] and d["prest_cnpj"] and d["emit_cnpj"] != d["prest_cnpj"] and d["tpEmit"] == "1":
        r.falha("DOC-04", "Emitente ≠ prestador embora tpEmit = 1 (prestador)", "infNFSe/emit x DPS/prest", "Leiaute", "alto")
    if d["toma"] is not None and d["toma_cnpj"] is None and d["toma_cpf"] is None and d["toma_nif"] is None and d["toma_cNaoNIF"] is None:
        r.falha("DOC-05", "Tomador sem identificação (CNPJ/CPF/NIF/cNaoNIF)", "DPS/infDPS/toma", "Leiaute: CNPJ obrigatório para PJ", "alto")

    # R12 — zeros não significativos
    zeros = [n for n in ("nNFSe", "nDFSe", "nDPS") if d.get(n) and d[n] != d[n].lstrip("0") and d[n].strip("0") != ""]
    if zeros:
        r.aviso("FMT-01", f"Zeros não significativos em {', '.join(zeros)}", "infNFSe / DPS", "Manual, seção 8.1 (formatos)", "baixo", "média")

    # R13 — transparência (Lei 12.741)
    if d["totTrib"] is not None:
        r.passa("TRP-01", "Grupo totTrib presente", "DPS/.../totTrib", "Lei 12.741/2012, art. 1º")
        if d["vTotTribMun"] is not None and d["vISSQN"] is not None and d["vISSQN"] > 0 and abs(d["vTotTribMun"] - d["vISSQN"]) > Decimal("0.05"):
            r.aviso("TRP-02", f"vTotTribMun {d['vTotTribMun']} ≠ vISSQN {d['vISSQN']} — tributo municipal informado em dois valores",
                    "DPS/.../vTotTribMun", "Lei 12.741/2012, art. 1º (valor aproximado admitido)", "baixo")
        if simples and d["vTotTribFed"] and d["vServ"] and d["vTotTribFed"] / d["vServ"] > Decimal("0.12"):
            r.aviso("TRP-03", f"vTotTribFed {d['vTotTribFed']} ({d['vTotTribFed']/d['vServ']*100:.2f}%) alto para optante do Simples (Anexo III inicia em 6% total)",
                    "DPS/.../vTotTribFed", "Lei 12.741/2012; LC 123, Anexo III", "baixo", "média", "usar pTotTribSN ou tabela IBPT do regime")
    elif d["toma"] is not None and (d["toma_cpf"] or d["toma_cnpj"]):
        r.aviso("TRP-01", "Sem totTrib nem indTotTrib", "DPS/.../totTrib", "Lei 12.741/2012, art. 1º", "baixo", "média")

    # R14 — IBS/CBS
    if d_comp and d_comp > DATA_IBSCBS_OBRIG and not d["ibscbs"]:
        r.falha("RTC-01", "Grupo IBSCBS ausente em competência posterior a 01/10/2026", "DPS/infDPS/IBSCBS",
                "NT 009/2026 (manual v1.01 rev. 03/08/2026)", "médio", "média")

    # R15 — assinatura / ambiente
    if not d["signature"]:
        r.aviso("ASS-01", "XML sem elemento Signature", "NFSe", "Manual, 7.3.5 (assinatura pela administração tributária)", "baixo", "média")
    if d["tpAmb"] != "1" or d["ambGer"] not in ("1", "2"):
        r.aviso("AMB-01", f"tpAmb {d['tpAmb']} / ambGer {d['ambGer']}", "DPS/tpAmb, infNFSe/ambGer", "Leiaute", "baixo")
    if d["xTribNac"] and p.get("item") and item_to_ctrib(p["item"]) not in ctrib:
        pass  # já reportado em SRV-01


# --- saída ------------------------------------------------------------------------------------

ORD = {"FALHA": 0, "AVISO": 1, "PASSA": 2}
RISCO = {"alto": 0, "médio": 1, "baixo": 2, None: 3}


def imprimir(rep, d, p):
    print(f"NFS-e {d['nNFSe']} | emit {d['emit_cnpj'] or d['emit_cpf']} | cTribNac {d['cTribNac']} | "
          f"vServ {d['vServ']} | ISS {d['vISSQN']} | opSimpNac {d['opSimpNac']} regAp {d['regApTribSN']} regEsp {d['regEspTrib']}")
    print("perfil:", "; ".join(f"{k}={v}" for k, v in p.items()))
    itens = sorted(rep.itens, key=lambda i: (ORD[i["resultado"]], RISCO[i["risco"]], i["codigo"]))
    atual = None
    for i in itens:
        if i["resultado"] != atual:
            atual = i["resultado"]
            print(f"\n== {atual} ==")
        tag = f"[{i['risco']}/{i['confianca']}]" if i["risco"] else f"[{i['confianca']}]"
        print(f"{i['codigo']:7} {tag:16} {i['mensagem']}")
        print(f"        onde: {i['onde']}")
        print(f"        norma: {i['norma']}")
        if i["correcao"]:
            print(f"        correção: {i['correcao']}")
    n = {k: sum(1 for i in rep.itens if i["resultado"] == k) for k in ORD}
    print(f"\n{n['FALHA']} falha(s), {n['AVISO']} aviso(s), {n['PASSA']} ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xml")
    ap.add_argument("perfil", nargs="?", help="linha de perfil (ou use --perfil arquivo)")
    ap.add_argument("--perfil", dest="perfil_arq")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    perfil = a.perfil or (open(a.perfil_arq, encoding="utf-8").read() if a.perfil_arq else "")
    if not perfil:
        sys.exit("informe a linha de perfil")
    p = parse_perfil(perfil)
    root = ET.parse(a.xml).getroot()
    if root.tag != "{%s}NFSe" % NS["n"]:
        sys.exit("raiz não é NFSe do namespace nacional")
    d = extrair(root)
    rep = Report()
    checar(d, p, rep)
    if a.json:
        print(json.dumps(rep.itens, ensure_ascii=False, indent=2))
    else:
        imprimir(rep, d, p)
    return 1 if any(i["resultado"] == "FALHA" for i in rep.itens) else 0


if __name__ == "__main__":
    sys.exit(main())
