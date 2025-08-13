import shapefile
import os
from collections import Counter

shp_path = r"data\WAP_SHP\wap.shp"
field_name = "Action_Sum"

sf = shapefile.Reader(shp_path)
fields = [f[0] for f in sf.fields[1:]]
field_index = fields.index(field_name)

records = sf.records()
shapes = sf.shapes()

empty_count = 0
for rec in records:
    val = rec[field_index]
    if val is None or str(val).strip() == "":
        empty_count += 1
        rec[field_index] = "Unspecified"

counts = Counter(rec[field_index] for rec in records)
total_rows = len(records)

for val, count in sorted(counts.items()):
    print(f"{val}: {count}")
print("Empty or null rows before update:", empty_count)
print("Total rows:", total_rows)

temp_path = shp_path.replace(".shp", "_temp.shp")
with shapefile.Writer(temp_path) as w:
    w.fields = sf.fields[1:]
    for shape, rec in zip(shapes, records):
        w.shape(shape)
        w.record(*rec)

sf.close()

for ext in [".shp", ".shx", ".dbf"]:
    os.remove(shp_path.replace(".shp", ext))
    os.rename(temp_path.replace(".shp", ext), shp_path.replace(".shp", ext))
