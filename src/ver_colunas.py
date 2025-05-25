import pandas as pd
df = pd.read_csv("../data/Enhanced_pizza_sell_data_2024-25.csv", sep=';')
print(df.columns.tolist())