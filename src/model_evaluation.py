from sklearn.metrics import accuracy_score

def evaluate_models(model_rf, model_svc, X_test, y_test):
    y_pred_rf = model_rf.predict(X_test)
    y_pred_svc = model_svc.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    acc_svc = accuracy_score(y_test, y_pred_svc)
    return acc_rf, acc_svc