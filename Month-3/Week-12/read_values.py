import rasterio
import numpy as np

with rasterio.open(r"Month-3\Month_3_starter_data\data\raw\dem.tif") as src:
    elevation = src.read(1)
    print("Array shape:", elevation.shape)
    print("Smallest:", elevation.min())

    elevation = src.read(1, masked=True)
    print("Smallest real value:", round(float(elevation.min()),1))
    print("Largest:", round(float(elevation.max()),1))
    print("Mean:", round(float(elevation.mean()),1))
    print("Nodata cells:", round(int(elevation.mask.sum()),1))