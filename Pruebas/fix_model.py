import joblib
from xgboost import XGBClassifier

# Cargar modelo con la versión anterior de XGBoost
modelo_xgb = joblib.load("modelo_voting.pkl")

# Re-guardar el modelo con la nueva versión de XGBoost
joblib.dump(modelo_xgb, "modelo_voting_fixed.pkl")

print("Modelo guardado nuevamente en formato PKL con la versión actual.")
