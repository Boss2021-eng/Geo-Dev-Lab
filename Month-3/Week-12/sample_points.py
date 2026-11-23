import rasterio
import geopandas as gpd

with rasterio.open(r"Month-3\Month_3_starter_data\data\raw\dem.tif") as src:
    facilities = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\facilities.gpkg", layer="facilities").to_crs(src.crs)
    coords = [(p.x, p.y) for p in facilities.geometry]
    facilities["elevation_m"] = [values[0] for values in src.sample(coords)]

    print(facilities[["name","elevation_m"]].head())