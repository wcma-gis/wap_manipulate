import csv
import os
import tempfile
from collections import Counter

csv_path = r"data\Master2.csv"
field_name = "Action Summary"

with open(csv_path, "r", newline="", encoding="utf-8") as f_in:
    reader = csv.reader(f_in)
    rows = list(reader)

header = rows[0]
idx = header.index(field_name)

empty_count = 0

counts = Counter(r[idx] for r in rows[1:])
total_rows = len(rows) - 1

for val, count in sorted(counts.items()):
    print(f"{val}: {count}")
print("Empty or null rows before update:", empty_count)
print("Total rows:", total_rows)
