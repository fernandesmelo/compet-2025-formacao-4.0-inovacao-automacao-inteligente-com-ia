from sklearn.metrics import accuracy_score

def avaliar_modelos(modelo_rf, modelo_svc, X_teste, y_teste):
    acc_rf = modelo_rf.score(X_teste, y_teste)
    acc_svc = modelo_svc.score(X_teste, y_teste)
    print(f"Acurácia RandomForest: {acc_rf*100:.2f}%")
    print(f"Acurácia SVC: {acc_svc*100:.2f}%")
    return acc_rf, acc_svc