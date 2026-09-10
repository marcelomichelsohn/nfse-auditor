#!/usr/bin/env python3
"""measure.py — measures the four report-format variants in this folder. Standard library only.

    python3 rounds/report-format-v2/measure.py        # run from the repo root (or from anywhere: paths are absolute)

What it prints, per variant, over the 8 data rows of the table (header and separator excluded):
  1. row width, max and mean (characters, not bytes)
  2. cumulative width of the first four columns (start of line .. closing pipe of the 4th cell), max and mean
  3. per row: the column at which the cumulative width first passes 100, 120 and 160 characters
  4. the largest cell per column (column name -> characters)
And then the real cost in the checker: it imports tools/check_audit.py, fills what main() fills
(LAYOUT from reference/tables/required-fields.md), and runs C1/C2 over each variant file, printing the
findings verbatim.
"""
import os, sys, statistics, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
VARIANTS = ["V0-as-is.md", "V1-enriched.md", "V2-enriched-reordered.md", "V3-enriched-short-location.md"]
THRESHOLDS = (100, 120, 160)


def table(path):
    """Returns (column names, [(line number, raw line)]) for the report table."""
    lines = open(path, encoding="utf-8").read().split("\n")
    header = cols = None
    rows = []
    for i, line in enumerate(lines, 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header, cols = i, cells
            continue
        if set(line) <= set("|- :"):          # the separator row
            continue
        rows.append((i, line))
    return cols, rows


def cells_of(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def cum_widths(line):
    """cum[k] = characters from the start of the line to the closing pipe of cell k+1, inclusive."""
    pipes = [i for i, ch in enumerate(line) if ch == "|"]
    return [p + 1 for p in pipes[1:]]


def measure(path):
    cols, rows = table(path)
    widths = [len(l) for _, l in rows]
    four = []
    crossings = []
    biggest = {c: 0 for c in cols}
    for ln, line in rows:
        cw = cum_widths(line)
        assert len(cw) == len(cols), f"{path}:{ln}: {len(cw)} cells, header has {len(cols)}"
        four.append(cw[3])
        row_cross = {}
        for t in THRESHOLDS:
            hit = next((cols[k] for k, w in enumerate(cw) if w > t), None)
            row_cross[t] = hit
        crossings.append((ln, cells_of(line)[1], row_cross))
        for c, v in zip(cols, cells_of(line)):
            biggest[c] = max(biggest[c], len(v))
    return dict(cols=cols, n=len(rows), max_w=max(widths), mean_w=statistics.mean(widths),
                max4=max(four), mean4=statistics.mean(four), crossings=crossings, biggest=biggest)


def load_checker():
    spec = importlib.util.spec_from_file_location("check_audit", os.path.join(ROOT, "tools", "check_audit.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules["check_audit"] = m
    spec.loader.exec_module(m)
    return m


def run_checker(mod, path):
    """What main() does, minus the parts C1/C2 do not read: ids, the two corpora, and LAYOUT."""
    mod.fails = []
    mod.kept_findings = []
    mod.KEPT.clear()
    ids = mod.index_ids()
    corp = {"pt": mod.corpus("pt"), "en": mod.corpus("en")}
    if not mod.LAYOUT:
        rf = os.path.join(ROOT, "reference", "tables", "required-fields.md")
        if os.path.exists(rf):
            mod.LAYOUT.append(mod.norm(mod.read(rf)))
    mod.c1_c2([path], ids, corp)
    return list(mod.fails), len(mod.report_rows(path))


def main():
    mod = load_checker()
    results = {}
    for v in VARIANTS:
        p = os.path.join(HERE, v)
        m = measure(p)
        m["fails"], m["rows_seen"] = run_checker(mod, p)
        results[v] = m

    print("=" * 78)
    print("1-2. ROW WIDTH AND FIRST FOUR COLUMNS (8 data rows per variant, characters)")
    print("=" * 78)
    print(f"{'variant':<32} {'max':>6} {'mean':>7} {'4col max':>9} {'4col mean':>10}")
    for v, m in results.items():
        print(f"{v:<32} {m['max_w']:>6} {m['mean_w']:>7.1f} {m['max4']:>9} {m['mean4']:>10.1f}")

    for v, m in results.items():
        print()
        print("=" * 78)
        print(f"3. WHERE THE CUMULATIVE WIDTH PASSES EACH THRESHOLD — {v}")
        print("=" * 78)
        print(f"{'line':>5}  {'check':<22} {'>100':<14} {'>120':<14} {'>160':<14}")
        for ln, chk, cr in m["crossings"]:
            short = (chk[:20] + "..") if len(chk) > 22 else chk
            print(f"{ln:>5}  {short:<22} " + " ".join(f"{str(cr[t]):<14}" for t in THRESHOLDS))
        print()
        print(f"4. LARGEST CELL PER COLUMN — {v}")
        for c in m["cols"]:
            print(f"   {c:<16} {m['biggest'][c]:>5}")

    print()
    print("=" * 78)
    print("5. CHECKER COST — tools/check_audit.py C1/C2 run over each variant file")
    print("=" * 78)
    for v, m in results.items():
        print()
        print(f"--- {v}  (rows the checker sees: {m['rows_seen']}; findings: {len(m['fails'])}) ---")
        if not m["fails"]:
            print("    (no C1/C2 findings)")
        for f in m["fails"]:
            print("   ", f)


if __name__ == "__main__":
    main()
