import geopandas as gpd
import matplotlib.pyplot as plt

Lagos_lga = gpd.read_file(r"week 3\Lagos_Health_and_LGA.gpkg", layer="lagos_lga")
facilities = gpd.read_file("Week 4\Lagos_lga_and_health.gpkg", layer="health_facilities__health_facilities_lagos")

# print(facilities)

fig, ax = plt.subplots(figsize=(7,8))
Lagos_lga.plot(ax=ax, color="#E6F2F3",edgecolor="#037e8e")
facilities.plot(ax=ax, color="#b71c17", markersize=1)
ax.set_title("Health Facilties in Ibadan North")
ax.set_axis_off()

fig.savefig(r"Month-3\Week-11\independent_challenge\lagos_health_facilities.png", dpi=400, bbox_inches = "tight")
print("Map Saved")