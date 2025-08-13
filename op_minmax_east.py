import pandas as pd
import re

def extract_first_number(s):
    s = str(s).replace(",", "")
    m = re.search(r"\d+", s)
    return float(m.group(0)) if m else None

df = pd.read_csv("data/Master6.csv")

eastings = df["Easting GDA 94"].apply(extract_first_number)
northings = df["Northing GDA 94"].apply(extract_first_number)

def show_min_max(series, ids, label):
    sorted_vals = series.sort_values()
    min_idx = sorted_vals.index[0]
    max_idx = sorted_vals.index[-1]
    second_min_idx = sorted_vals.index[1]
    second_max_idx = sorted_vals.index[-2]
    print(f"{label} min: {series[min_idx]} ({ids[min_idx]})")
    print(f"{label} 2nd min: {series[second_min_idx]} ({ids[second_min_idx]})")
    print(f"{label} max: {series[max_idx]} ({ids[max_idx]})")
    print(f"{label} 2nd max: {series[second_max_idx]} ({ids[second_max_idx]})")

show_min_max(eastings, df["Site ID"], "Easting")
show_min_max(northings, df["Site ID"], "Northing")
