import geopandas as gpd
from shapely.geometry import Polygon
from shapely.validation import explain_validity

Lagos_lga = gpd.read_file(r"week 3\Lagos_Health_and_LGA.gpkg", layer="lagos_lga")
print("Valid now:", Lagos_lga.is_valid.all())

