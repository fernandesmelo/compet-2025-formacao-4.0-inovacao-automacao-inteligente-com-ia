from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_models(X_train, y_train):
    model_rf = RandomForestClassifier(n_estimators=200, random_state=42)
    model_svc = SVC(kernel='linear', random_state=42)
    model_rf.fit(X_train, y_train)
    model_svc.fit(X_train, y_train)
    return model_rf, model_svc