import pandas as pd

input_path = r"data\Master3.csv"
output_ok = r"data\Master4_ok.csv"
output_bad = r"data\Master4_bad.csv"

lat_col = "lat"
lon_col = "lon"

df = pd.read_csv(input_path, dtype=str, keep_default_na=False)
df[lat_col] = df[lat_col].str.strip()
df[lon_col] = df[lon_col].str.strip()

df_ok = df[(df[lat_col] != "") & (df[lon_col] != "")]
df_bad = df[(df[lat_col] == "") | (df[lon_col] == "")]

df_ok.to_csv(output_ok, index=False)
df_bad.to_csv(output_bad, index=False)
