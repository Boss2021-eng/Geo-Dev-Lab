import pandas as pd

pop = pd.read_csv(r"Month-3\Month_3_starter_data\data\raw\ward_population.csv")

big = pop[pop['population_2024'] > 35000]

print(big)

print("Wards over 35,000:", len(big))

# ranking
ranked = pop.sort_values('population_2024', ascending=False)
print(ranked.head())

pop["population_thousands"] = pop['population_2024']/1000
print(pop.head(3))
print("Total Population", pop['population_2024'].sum())