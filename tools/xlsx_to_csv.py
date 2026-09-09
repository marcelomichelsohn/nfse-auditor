#!/usr/bin/env python3
"""xlsx_to_csv.py — one-off conversion of the official .xlsx annexes to CSV, one file per sheet, so they can be loaded
into a Claude project (which reads CSV and refuses .zip; .xlsx loads poorly). The .xlsx stay the official files, hashed in
official/SHA256SUMS.txt; the CSVs are a conversion made by the author on the date in official/csv/SHA256SUMS.txt.
Needs openpyxl (not standard library) — run by the author once; a reader does not need to run it.

    python3 tools/xlsx_to_csv.py            # writes reference/tables/official/csv/<xlsx-stem>__<sheet>.csv + SHA256SUMS.txt
"""
import os, csv, glob, hashlib, re, datetime
import openpyxl

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "reference", "tables", "official")
DST = os.path.join(SRC, "csv")
os.makedirs(DST, exist_ok=True)
sums = []
for x in sorted(glob.glob(os.path.join(SRC, "*.xlsx"))):
    wb = openpyxl.load_workbook(x, read_only=True, data_only=True)
    stem = os.path.splitext(os.path.basename(x))[0]
    for ws in wb.worksheets:
        sheet = re.sub(r"[^A-Za-z0-9_-]+", "_", ws.title).strip("_") or "sheet"
        out = os.path.join(DST, f"{stem}__{sheet}.csv")
        n = 0
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for row in ws.iter_rows(values_only=True):
                if row is None or all(v is None or str(v).strip() == "" for v in row): continue
                w.writerow(["" if v is None else str(v).replace("\n", " ").strip() for v in row]); n += 1
        h = hashlib.sha256(open(out, "rb").read()).hexdigest()
        sums.append(f"{h}  {os.path.basename(out)}")
        print(f"{os.path.basename(out)}: {n} rows")
with open(os.path.join(DST, "SHA256SUMS.txt"), "w") as f:
    f.write(f"# CSV conversion of the official .xlsx in ../ (sources hashed in ../SHA256SUMS.txt), made {datetime.date.today().isoformat()} by tools/xlsx_to_csv.py\n")
    f.write("\n".join(sums) + "\n")
