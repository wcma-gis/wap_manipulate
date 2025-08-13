import pandas as pd
import re
from pyproj import Transformer

df = pd.read_csv("WAP.csv", encoding="ISO-8859-1")
transformer = Transformer.from_crs("EPSG:28354", "EPSG:4326", always_xy=True)

def extract_first_number_6_or_more_digits(s):
    matches = re.findall(r"\b\d{6,}\b", str(s))
    return float(matches[0]) if matches else None

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
df["Site ID"] = [f"WAP_2025_07_{i:06d}" for i in range(1, len(df) + 1)]
df.to_csv("WAP2.csv", index=False)
