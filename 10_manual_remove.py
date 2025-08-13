import pandas as pd

df = pd.read_csv("data/Master6.csv")
df = df[df["Site ID"] != "WAP_2025_07_000028"]
df.to_csv("data/Master7.csv", index=False)
