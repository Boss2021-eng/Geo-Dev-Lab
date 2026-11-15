import geopandas as gpd


Lagos_lga = gpd.read_file(r"week 3\Lagos_Health_and_LGA.gpkg", layer="lagos_lga")
facilities = gpd.read_file("Week 4\Lagos_lga_and_health.gpkg", layer="health_facilities__health_facilities_lagos")


# count the facilities per ward
joined = gpd.sjoin(facilities, Lagos_lga[["adm2_name", "geometry"]], how="inner", predicate="within")

counts = joined.groupby("adm2_name").size().rename("facility_count").reset_index()
print(counts)
# print(facilities.head())
print("Total Facilities", counts["facility_count"].sum(), "of", len(facilities))