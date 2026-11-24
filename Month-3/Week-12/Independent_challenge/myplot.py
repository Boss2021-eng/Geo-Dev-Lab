import matplotlib.pyplot as plt
import rasterio

with rasterio.open(r"Month-3\Week-12\Independent_challenge\ndwi.tif") as src:
    ndwi = src.read(1, masked=True)

fig, ax = plt.subplots(figsize=(7,8))
image = ax.imshow(
    ndwi,
    cmap="BrBG",
    vmin=-1,
    vmax=1
)

fig.colorbar(image, ax=ax, label="NDWI")

ax.set_title("Normalized Difference Water Index, Lagos")
ax.set_axis_off()

ax.set_axis_off()
fig.savefig("Month-3\Week-12\Independent_challenge/ndwi_map.png" , dpi=150, bbox_inches="tight")
print("Saved ndwi_map.png")