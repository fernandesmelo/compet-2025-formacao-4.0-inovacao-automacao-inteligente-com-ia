import pandas as pd

df = pd.read_csv("../data/Enhanced_pizza_sell_data_2024-25.csv", sep=',')

df.loc[:4, 'Delay (min)'] = 0

df['Delay (min)'] = pd.to_numeric(df['Delay (min)'].astype(str).str.strip().str.replace('"', ''), errors='coerce').fillna(0)
df['Is Delayed'] = df['Delay (min)'].apply(lambda x: 1 if x > 0 else 0)

df.to_csv("../data/Enhanced_pizza_sell_data_2024-25.csv", index=False)

print("Coluna 'Is Delayed' preenchida automaticamente!")