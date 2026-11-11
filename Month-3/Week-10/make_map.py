import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")
facilities = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\facilities.gpkg", layer="facilities")

# print(facilities)

fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2F3",edgecolor="#037e8e")
facilities.plot(ax=ax, color="#b71c17", markersize=18)
ax.set_title("Health Facilties in Ibadan North")
ax.set_axis_off()

fig.savefig(r"Month-3\Week-10\facilities_map.png", dpi=150, bbox_inches = "tight")
print("Map Saved")