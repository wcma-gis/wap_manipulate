import csv
import os

input_path = r"data\Master3.csv"
output_ok = r"data\Master4_ok.csv"
output_bad = r"data\Master4_bad.csv"

lat_col = "lat"
lon_col = "lon"

with open(input_path, "r", newline="", encoding="latin-1") as f_in:
    reader = csv.reader(f_in)
    rows = list(reader)

header = rows[0]
lat_idx = header.index(lat_col)
lon_idx = header.index(lon_col)

ok_rows = [header]
bad_rows = [header]

for r in rows[1:]:
    lat_val = str(r[lat_idx]).strip()
    lon_val = str(r[lon_idx]).strip()
    if lat_val == "" or lon_val == "":
        bad_rows.append(r)
    else:
        ok_rows.append(r)

with open(output_ok, "w", newline="", encoding="latin-1") as f_ok:
    csv.writer(f_ok).writerows(ok_rows)

with open(output_bad, "w", newline="", encoding="latin-1") as f_bad:
    csv.writer(f_bad).writerows(bad_rows)
