import shapefile
import os

shp_path = r"data\WAP_SHP\wap.shp"
field_name = "Action_Sum"

mapping = {
    "Fence & Revege": "Fence & Revege",
    "Fence & Revegetate to improve Ecology": "Fence & Revege",
    "Fence & revegetate to improve ecology": "Fence & Revege",
    "Fence & revegetate to improve habitat": "Fence & Revege",
    "Fence & revegetate to improve vegetation": "Fence & Revege"
}

sf = shapefile.Reader(shp_path)
fields = [f[0] for f in sf.fields[1:]]
field_index = fields.index(field_name)

records = sf.records()
shapes = sf.shapes()

for rec in records:
    val = rec[field_index]
    if val in mapping:
        rec[field_index] = mapping[val]

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
