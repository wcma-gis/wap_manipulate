import pandas as pd
import re
from pyproj import Transformer

def extract_first_number_6_or_more_digits(s):
    s = str(s).replace(",", "")
    m = re.search(r"\d{6,}", s)
    return float(m.group(0)) if m else None

df = pd.read_csv("data/Master4_ok.csv")

affected_ids = set()

df.loc[df["Site ID"] == "WAP_2025_07_000026", "Northing GDA 94"] = 5934862
affected_ids.add("WAP_2025_07_000026")
df.loc[df["Site ID"] == "WAP_2025_07_000027", "Northing GDA 94"] = 5934762
affected_ids.add("WAP_2025_07_000027")

def fix_northing(row):
    s = str(row["Northing GDA 94"]).replace(",", "")
    m = re.search(r"\d{6,}", s)
    if not m:
        return row["Northing GDA 94"]
    t = m.group(0)
    if len(t) == 6:
        affected_ids.add(row["Site ID"])
        t = t + "0"
    return float(t)

df["Northing GDA 94"] = df.apply(fix_northing, axis=1)

transformer = Transformer.from_crs("EPSG:28354", "EPSG:4326", always_xy=True)
eastings = df["Easting GDA 94"].apply(extract_first_number_6_or_more_digits)
northings = df["Northing GDA 94"].apply(extract_first_number_6_or_more_digits)

valid = eastings.notna() & northings.notna()
lons, lats = [None] * len(df), [None] * len(df)
lons_valid, lats_valid = transformer.transform(eastings[valid].values, northings[valid].values)
for i, idx in enumerate(df[valid].index):
    lons[idx] = lons_valid[i]
    lats[idx] = lats_valid[i]

df["lon"] = lons
df["lat"] = lats

df.to_csv("data/Master5.csv", index=False)
with open("6_hard_change_log.txt", "w") as f:
    for site_id in sorted(affected_ids):
        f.write(site_id + "\n")
