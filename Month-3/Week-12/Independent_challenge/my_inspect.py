import rasterio

with rasterio.open(r"Geo-Dev-Lab\Month-3\Week-12\Independent_challenge\n06_e003_1arc_v3.tif") as src:
    print("width x height", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("No data:", src.nodata)
    print("Transform")
    print(src.transform)