import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open(r"Month-3\Month_3_starter_data\data\raw\dem.tif") as src:
    wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards").to_crs(src.crs)
    means = []

    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means,1)
print(wards[["ward_name", "mean_elevation_m"]])