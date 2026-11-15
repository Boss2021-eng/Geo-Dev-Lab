import geopandas as gpd

Lagos_adm_boundaries = gpd.read_file(r"Week 4\Lagos_lga_and_health.gpkg", layer="lagos_adm_boundaries")


print("CRS", Lagos_adm_boundaries.crs)
print("CRS", Lagos_adm_boundaries.head())
# To estimate crs
print("Suggested UTM:", Lagos_adm_boundaries.estimate_utm_crs())

# Reproject your data into wards_utm
lagos_utm = Lagos_adm_boundaries.to_crs(epsg=32631)
lagos_utm["area_km2"] = lagos_utm.area/1000000
print(lagos_utm[["adm1_name", "area_km2"]].head(3)) 
print("Lagos :", round(lagos_utm["area_km2"].sum(), 2), "km2")