import geopandas as gpd

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")
wards.to_file(r"Month-3\Month_3_starter_data\data\processed\week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv(r"Month-3\Month_3_starter_data\data\processed\wards_table.csv", index=False)

print(gpd.list_layers(wards))