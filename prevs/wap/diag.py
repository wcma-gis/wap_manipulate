import pandas as pd
import re

df = pd.read_csv("WAP.csv", encoding="ISO-8859-1")

def extract_first_six_digit(s):
    matches = re.findall(r"\b\d{6}\b", str(s))
    return matches[0] if matches else None

print("Easting col name:", repr(df.columns[df.columns.str.contains("Easting")][0]))
print("Northing col name:", repr(df.columns[df.columns.str.contains("Northing")][0]))
print("First row Easting raw:", df.iloc[0][df.columns[df.columns.str.contains("Easting")][0]])
print("First row Northing raw:", df.iloc[0][df.columns[df.columns.str.contains("Northing")][0]])
print("Parsed Easting:", extract_first_six_digit(df.iloc[0][df.columns[df.columns.str.contains("Easting")][0]]))
print("Parsed Northing:", extract_first_six_digit(df.iloc[0][df.columns[df.columns.str.contains("Northing")][0]]))
