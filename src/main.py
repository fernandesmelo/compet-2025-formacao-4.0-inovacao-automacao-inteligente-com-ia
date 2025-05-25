import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

from data_preprocessing import carregar_e_preprocessar_dados
from model_training import treinar_modelos
from model_evaluation import avaliar_modelos
from utils import grafico_barra, grafico_pizza, grafico_dispersao

caminho_csv = "../data/Enhanced_pizza_sell_data_2024-25.csv"
X, y, df = carregar_e_preprocessar_dados(caminho_csv)

grafico_barra(df, "Pizza Size", "Distribuição dos Tamanhos de Pizza")
grafico_pizza(df, "Traffic Level", "Nível de Tráfego nos Pedidos")
grafico_dispersao(df, "Distance (km)", "Delivery Efficiency (min/km)", "Distância vs Eficiência de Entrega")

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_rf, modelo_svc = treinar_modelos(X_treino, y_treino)

acc_rf, acc_svc = avaliar_modelos(modelo_rf, modelo_svc, X_teste, y_teste)

with open("../model/best_model.pkl", "wb") as f:
    pickle.dump(modelo_rf if acc_rf > acc_svc else modelo_svc, f)

print("Modelo salvo com sucesso!")