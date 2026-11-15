import geopandas as gpd

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")

# Picking first points of the first ward geometry
first = wards.geometry.iloc[0].exterior.coords[0]
print("Original first corner", first)

# After reprojecting the coordinate
projected = wards.to_crs(epsg=32631)
print("After to_crs", projected.geometry.iloc[0].exterior.coords[0])

# After assigning or relabelling the coordinate
wrongly_labelled = wards.set_crs(epsg=32631, allow_override=True)
print("After set crs", wrongly_labelled.geometry.iloc[0].exterior.coords[0])
print("Label now say", wrongly_labelled.crs)

wrongly_labelled.to_file(r"Month-3\Month_3_starter_data\data\processed\wards_wrongly_labelled.gpkg", layer="wards")