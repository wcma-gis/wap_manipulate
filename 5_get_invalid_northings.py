import pandas as pd
import re

def extract_first_number_6_or_more_digits(s):
    s = str(s).replace(",", "")
    m = re.search(r"\d{6,}", s)
    return m.group(0) if m else None

df = pd.read_csv("data/Master4_ok.csv")
parsed = df["Northing GDA 94"].apply(extract_first_number_6_or_more_digits)
df["Parsed Northing"] = parsed
bad = df.loc[parsed.isna() | (parsed.str.len() != 7), ["Site ID", "Parsed Northing", "Northing GDA 94"]]
print(bad)
