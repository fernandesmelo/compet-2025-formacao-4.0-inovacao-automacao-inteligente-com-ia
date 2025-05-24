import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

from data_preprocessing import load_and_preprocess_data
from model_training import train_models
from model_evaluation import evaluate_models
from utils import plot_bar, plot_pie, plot_scatter

csv_path = "../data/Enhanced_pizza_sell_data_2024-25.csv"
X, y, df = load_and_preprocess_data(csv_path)

plot_bar(df, "Pizza Size", "Distribuição dos tamanhos de pizza")
plot_pie(df, "Traffic Level", "Nível de tráfego nos pedidos")
plot_scatter(df, "Distance (km)", "Delivery Efficiency (min/km)", "Distância vs Eficiência de Entrega")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_rf, model_svc = train_models(X_train, y_train)

acc_rf, acc_svc = evaluate_models(model_rf, model_svc, X_test, y_test)
print(f"Acurácia RandomForest: {acc_rf*100:.2f}%")
print(f"Acurácia SVC: {acc_svc*100:.2f}%")

best_model = model_rf if acc_rf > acc_svc else model_svc
with open("../model/best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)
print("Modelo salvo com sucesso!")