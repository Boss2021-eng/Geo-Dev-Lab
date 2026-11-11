import geopandas as gpd

Lagos_adm_boundaries = gpd.read_file(r"Week 4\Lagos_lga_and_health.gpkg", layer="lagos_adm_boundaries")

print(Lagos_adm_boundaries.head())
print("Rows and Columns", Lagos_adm_boundaries.shape)
print(Lagos_adm_boundaries.geom_type.value_counts())
print("CRS", Lagos_adm_boundaries.crs)
print("Bounds", Lagos_adm_boundaries.total_bounds)