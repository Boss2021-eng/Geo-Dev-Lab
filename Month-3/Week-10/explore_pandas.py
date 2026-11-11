# Import the required libraries
import pandas as pd

# pop = pd.read_csv(r"./Month 3/Month_3_starter_data/data/raw/ward_population.csv")

pop = pd.read_csv(r"Month-3\Month_3_starter_data\data\raw\ward_population.csv")

print(pop.head(7))
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
print(pop['population_2024'].describe())