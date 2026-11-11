import pandas as pd
import geopandas as gpd

table = pd.read_csv(r"Month-3\Month_3_starter_data\data\raw\health_facilities.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs = "EPSG:4326"
)

print(facilities.head(3))
print(facilities.crs)

facilities.to_file(r"Month-3\Month_3_starter_data\data\processed\facilities.gpkg", layer="facilities")
print("saved", len(facilities), "facilities")