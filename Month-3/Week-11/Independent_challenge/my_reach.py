import geopandas as gpd


Lagos_lga = gpd.read_file(r"week 3\Lagos_Health_and_LGA.gpkg", layer="lagos_lga")
facilities = gpd.read_file("Week 4\Lagos_lga_and_health.gpkg", layer="health_facilities__health_facilities_lagos")

print(facilities.head())
print(facilities.columns)
# get the center of the LGAs
centres = Lagos_lga[["adm2_name", "geometry"]].copy()
centres["geometry"] = Lagos_lga.centroid

nearest = gpd.sjoin_nearest(
    centres, 
    facilities[["prmry_name", "geometry"]],
    how="left",
    distance_col="distance_m"
)
nearest["distance_km"] = (nearest["distance_m"]/1000).round(2)
print(nearest[[ "adm2_name","prmry_name", "distance_km"]])
