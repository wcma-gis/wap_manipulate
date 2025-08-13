import csv
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

with open(csv_path, "r", newline="", encoding="latin-1") as f_in:
    reader = csv.reader(f_in)
    rows = list(reader)

header = rows[0]
idx = header.index(field_name)

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(csv_path), suffix=".csv")
os.close(fd)

with open(tmp_path, "w", newline="", encoding="latin-1") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(header)
    for r in rows[1:]:
        if r[idx] is None or str(r[idx]).strip() == "":
            r[idx] = "Unspecified"
        elif r[idx] in mapping:
            r[idx] = mapping[r[idx]]
        r[idx] = r[idx].strip()
        r = [c.strip() if isinstance(c, str) else c for c in r]
        writer.writerow(r)

os.replace(tmp_path, output_path)
