import pandas as pd
import re

def extract_first_number(s):
    s = str(s).replace(",", "")
    m = re.search(r"\d+", s)
    return float(m.group(0)) if m else None

df = pd.read_csv("data/Master5.csv")
eastings = df["Easting GDA 94"].apply(extract_first_number)
print(eastings.min(), eastings.max())

northings = df["Northing GDA 94"].apply(extract_first_number)
print(northings.min(), northings.max())