import pandas as pd
import os
import tempfile

csv_path = r"data\Master.csv"
output_path = r"data\Master2.csv"
field_name = "Action Summary"

mapping = {
    "Control Spiny rush": "Control Spiny Rush",
    "Establish wetland to improve Water Quality": "Establish Wetland to Improve Water Quality",
    "Fence & Revege": "Fencing & Revegetation",
    "Fence & Revegetate to improve Ecology": "Fencing & Revegetation",
    "Fence & revegetate to improve ecology": "Fencing & Revegetation",
    "Fence & revegetate to improve habitat": "Fencing & Revegetation",
    "Fence & revegetate to improve vegetation": "Fencing & Revegetation",
    "Fencing & Revegetation": "Fencing & Revegetation",
    "Fencing & revegetation": "Fencing & Revegetation",
    "Fence / Offstream watering": "Fence & Offstream Watering",
    "Fence to protect platypus": "Fence to Protect Platypus",
    "Platypus & water quality monitoring": "Platypus & Water Quality Monitoring",
    "Platypus & water quality/biological monitoring": "Platypus & Water Quality/Biological Monitoring",
    "Platypus & Water Quality/Biological Monitoring": "Platypus & Water Quality Monitoring",
    "Platypus study": "Platypus Study",
    "Water Quality": "Water Quality Monitoring",
    "Water Quality monitoring": "Water Quality Monitoring",
    "Water quality monitoring": "Water Quality Monitoring",
    "Wetland to improve water quality": "Wetland to Improve Water Quality",
    "Vegetate": "Vegetation",
    "Fence & Revegetate": "Fencing & Revegetation",
    "Flood signage": "Flood Signage",
    "Investigate": "Investigation",
    "Monitor": "Monitoring",
    "Wetland to Improve Water Quality": "Establish Wetland to Improve Water Quality"
}

df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()
df[field_name] = df[field_name].replace("", "Unspecified").map(lambda v: mapping.get(v, v))

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(csv_path), suffix=".csv")
os.close(fd)
df.to_csv(tmp_path, index=False)
os.replace(tmp_path, output_path)
