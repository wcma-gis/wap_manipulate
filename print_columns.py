import shapefile

shp_path = r"data\WAP_SHP\wap.shp"

sf = shapefile.Reader(shp_path)
fields = [f[0] for f in sf.fields[1:]]  # skip DeletionFlag
for name in fields:
    if "action" in name.lower():
        print(f"|{name}|")
