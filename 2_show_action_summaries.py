import pandas as pd

csv_path = r"data\Master2.csv"
field_name = "Action Summary"

df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
s = df[field_name].fillna("").astype(str).str.strip()

empty_count = (s == "").sum()
total_rows = len(s)

counts = s.value_counts(dropna=False)

for val in sorted(counts.index, key=lambda x: str(x)):
    print(f"{val}: {counts[val]}")
print("Empty or null rows before update:", empty_count)
print("Total rows:", total_rows)
