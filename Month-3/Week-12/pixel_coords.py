import rasterio

with rasterio.open(r"Month-3\Month_3_starter_data\data\raw\dem.tif") as src:
    x,y = src.xy(0,0)
    print("Centre of top-left pixel", round(x,1), round(y,1))

    row, col = src.index(600000, 200000)
    print("That location is row", row, "column is", col)