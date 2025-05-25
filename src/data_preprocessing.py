import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path, sep=',')
    df.columns = df.columns.str.strip()
    cols = [
        "Pizza Size", "Pizza Type", "Toppings Count", "Distance (km)",
        "Traffic Level", "Payment Method", "Is Peak Hour", "Is Weekend",
        "Delivery Efficiency (min/km)", "Is Delayed"
    ]
    df = df[cols]
    df = df.dropna()
    le = LabelEncoder()
    for col in ["Pizza Size", "Pizza Type", "Traffic Level", "Payment Method"]:
        df[col] = le.fit_transform(df[col])
    for col in ["Is Peak Hour", "Is Weekend", "Is Delayed"]:
        df[col] = df[col].fillna(0).astype(int)
    X = df.drop("Is Delayed", axis=1)
    y = df["Is Delayed"]
    return X, y, df