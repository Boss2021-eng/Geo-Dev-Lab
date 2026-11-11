import pandas as pd
import geopandas as gpd

table = pd.read_csv(r"Month-3\health_facilities_lagos.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["X"], table["Y"]),
    crs = "EPSG:4326"
)

print(facilities.head(3))
print(facilities.crs)

facilities.to_file(r"Month-3\Week-10\Independent_challenge\files\facilities_independent.gpkg", layer="facilities")
print("saved", len(facilities), "facilities")