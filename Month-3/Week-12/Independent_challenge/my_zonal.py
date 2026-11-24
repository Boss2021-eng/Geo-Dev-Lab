
import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

# Read DEM
with rasterio.open(
    r"Month-3\Week-12\Independent_challenge\n06_e003_1arc_v3.tif"
) as src:

    # Read health facilities and match CRS
    facilities = gpd.read_file(
        "Week 4\Lagos_lga_and_health.gpkg",
        layer="health_facilities__health_facilities_lagos"
    ).to_crs(src.crs)

    means = []

    # Calculate mean elevation for each geometry
    for geom in facilities.geometry:

        cells, _ = mask(
            src,
            [geom],
            crop=True,
            filled=False
        )

        valid_cells = cells.compressed()

        if len(valid_cells) > 0:
            means.append(float(valid_cells.mean()))
        else:
            means.append(np.nan)

# Add results to GeoDataFrame
facilities["mean_elevation_m"] = np.round(means, 1)

print(facilities[["ward_name", "mean_elevation_m"]])
