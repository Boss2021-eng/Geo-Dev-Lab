import pandas as pd
import geopandas as gpd

wards = gpd.read_file(r"Month-3\Month_3_starter_data\data\processed\wards.gpkg", layer="wards")
pop = pd.read_csv(r"Month-3\Month_3_starter_data\data\raw\ward_population.csv")

first_try = wards.merge(pop,how="left",left_on="ward_name", right_on="ward")
matched = first_try["population_2024"].notna().sum()
print("Matched on first try", matched, "of", len(wards))
print(wards)
print(pop)

# print(wards["ward_name"].unique())
# for x, y in zip (wards["ward_name"].unique(), pop["ward"].unique()):
#     print( x,"-",y,"b")

def clean_name(name):
    return name.strip().upper().replace("-", " ")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)


joined= wards.merge(pop,how="left", on="join_key")
matched = joined["population_2024"].notna().sum()

print("matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_name", "population_2024"]])