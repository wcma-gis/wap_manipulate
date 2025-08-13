import shapefile
import os

shp_path = r"data\WAP_SHP\wap.shp"
field_name = "Action_Sum"

mapping = {
    "Control Spiny rush": "Control Spiny Rush",
    "Establish wetland to improve Water Quality": "Establish Wetland to Improve Water Quality",
    "Fence & Revege": "Fencing & Revegetation",
    "Fence & Revegetate to improve Ecology": "Fencing & Revegetation",
    "Fence & revegetate to improve ecology": "Fencing & Revegetation",
    "Fence & revegetate to improve habitat": "Fencing & Revegetation",
    "Fence & revegetate to improve vegetation": "Fencing & Revegetation",
    "Fencing & Revegetation" : "Fencing & Revegetation",
    "Fencing & revegetation" : "Fencing & Revegetation",
    "Fence / Offstream watering" : "Fence & Offstream Watering",
    "Fence to protect platypus" : "Fence to Protect Platypus",
    "Platypus & water quality monitoring" : "Platypus & Water Quality Monitoring",
    "Platypus & water quality/biological monitoring" : "Platypus & Water Quality/Biological Monitoring",
    "Platypus & Water Quality/Biological Monitoring" : "Platypus & Water Quality Monitoring",
    "Platypus study" : "Platypus Study",
    "Water Quality" : "Water Quality Monitoring",
    "Water Quality monitoring" : "Water Quality Monitoring",
    "Water quality monitoring" : "Water Quality Monitoring",
    "Wetland to improve water quality" : "Wetland to Improve Water Quality",
    "Vegetate" : "Vegetation",
    "Fence & Revegetate" : "Fencing & Revegetation",
    "Flood signage" : "Flood Signage",
    "Investigate" : "Investigation",
    "Monitor" : "Monitoring",
    "Wetland to Improve Water Quality" : "Establish Wetland to Improve Water Quality"


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
