import pandas as pd
import geopandas as gpd

Lagos_LGA = gpd.read_file(r"Week 2\Lagos LGA\Lagos_LGA.shp")
Lagos_LGA_pop= pd.read_csv(r"Week 2\LGA Population & Demographic Data\LGAs in Lagos State.csv")

print(Lagos_LGA.head())
print(Lagos_LGA_pop.head())

# print(Lagos_LGA_pop.columns)

first_try = Lagos_LGA.merge(Lagos_LGA_pop,how="left",left_on="adm2_name", right_on="LGAs")
matched = first_try[' Estimated Population 2024(Km 2) '].notna().sum()
print("Matched on first try", matched, "of", len(Lagos_LGA))
print(Lagos_LGA)
print(Lagos_LGA_pop)
