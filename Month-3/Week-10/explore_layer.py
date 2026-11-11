import geopandas as gpd

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")

print(wards.head())
print("Rows and Columns", wards.shape)
print(wards.geom_type.value_counts())
print("CRS", wards.crs)
print("Bounds", wards.total_bounds)