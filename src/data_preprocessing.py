import pandas as pd
from sklearn.preprocessing import LabelEncoder

def carregar_e_preprocessar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=',')
    df.columns = df.columns.str.strip()
    colunas = [
        "Pizza Size", "Pizza Type", "Toppings Count", "Distance (km)",
        "Traffic Level", "Payment Method", "Is Peak Hour", "Is Weekend",
        "Delivery Efficiency (min/km)", "Is Delayed"
    ]
    df = df[colunas]
    codificador = LabelEncoder()
    for coluna in ["Pizza Size", "Pizza Type", "Traffic Level", "Payment Method"]:
        df[coluna] = codificador.fit_transform(df[coluna])
    for coluna in ["Is Peak Hour", "Is Weekend", "Is Delayed"]:
        df[coluna] = df[coluna].fillna(0).astype(int)
    X = df.drop("Is Delayed", axis=1)
    y = df["Is Delayed"]
    print(df["Is Delayed"].value_counts())
    return X, y, df