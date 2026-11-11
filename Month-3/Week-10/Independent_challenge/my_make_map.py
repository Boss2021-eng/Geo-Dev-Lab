import geopandas as gpd
import matplotlib.pyplot as plt

Lagos_adm_boundaries = gpd.read_file(r"Week 4\Lagos_lga_and_health.gpkg", layer="lagos_adm_boundaries")
facilities = gpd.read_file(r"Week 4\Lagos_lga_and_health.gpkg", layer="health_facilities__health_facilities_lagos" )

# print(gpd.list_layers(r"Week 4\Lagos_lga_and_health.gpkg"))
# print(facilities)

fig, ax = plt.subplots(figsize=(10,7))
Lagos_adm_boundaries.plot(ax=ax, color="#E6F2F3",edgecolor="#037e8e")
facilities[0:20].plot(ax=ax, color="#b71c17", markersize=18)
ax.set_title("Health Facilities in Lagos")
ax.set_axis_off()

fig.savefig(r"Month-3\Week-10\Independent_challenge\files\lagos_facilities_map.png", dpi=300, bbox_inches = "tight")
print("Map Saved")

