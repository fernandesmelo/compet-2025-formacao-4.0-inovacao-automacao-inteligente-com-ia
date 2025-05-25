import pandas as pd

df = pd.read_csv("../data/Enhanced_pizza_sell_data_2024-25.csv", sep=',')

df['Is Delayed'] = df['Delay (min)'].apply(lambda x: 1 if pd.to_numeric(x, errors='coerce') > 0 else 0)

df.to_csv("../data/Enhanced_pizza_sell_data_2024-25.csv", index=False)

print("Coluna 'Is Delayed' preenchida automaticamente!")