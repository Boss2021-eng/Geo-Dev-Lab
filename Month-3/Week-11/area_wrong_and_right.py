import geopandas as gpd

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")
print("CRS", wards.crs)

# to get areas of wards in geographic coordinate system
wards["area_wrong"] = wards.area
print(wards[["ward_name", "area_wrong"]].head(3)) 

# To estimate crs
print("Suggested UTM:", wards.estimate_utm_crs())

# Reproject your data into wards_utm
wards_utm = wards.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area/1000000
print(wards_utm[["ward_name", "area_km2"]].head(3)) 
print("Ibadan North Total:", round(wards_utm["area_km2"].sum(), 2), "km2")