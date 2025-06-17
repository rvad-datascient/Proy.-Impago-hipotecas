
# 🏠 Predicción de Impagos Hipotecarios con Machine Learning

Este proyecto utiliza técnicas avanzadas de Machine Learning para predecir la probabilidad de que un cliente incurra en impagos hipotecarios.
Aunque se trata de un caso simulado, los datos provienen del conjunto "Give Me Some Credit" publicado en Kaggle, ampliamente utilizado para problemas de scoring crediticio. Es una solución completa que incluye limpieza de datos, preprocesamiento, optimización de modelos y despliegue mediante una aplicación web con Streamlit.

---

## 📌 Objetivo

Desarrollar un modelo predictivo que permita a entidades financieras **anticipar impagos** en solicitudes de créditos hipotecarios, ayudando así en la gestión de riesgo y toma de decisiones.

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- Scikit-learn
- XGBoost, LightGBM, CatBoost
- Optuna (optimización de hiperparámetros)
- SMOTE (balanceo de clases)
- Streamlit (para la aplicación web)
- SHAP (interpretabilidad del modelo)

---

## 📁 Estructura del proyecto

```
ml_project/
├── app.py                    # App de predicción con Streamlit
├── modelo_voting.pkl         # Modelo VotingClassifier final
├── scaler_robust.pkl         # Escalador robusto para transformar inputs
├── requirements.txt          # Librerías necesarias
├── README.md                 # Este archivo
├── data/
│   └── cs-training.csv       # Dataset original (Kaggle)
├── src/
│   ├── limpieza_basica.py
│   ├── division_datos.py
│   └── preprocesamiento.py
└── notebooks/
    └── exploratory.ipynb     # Análisis exploratorio y pruebas
```

---

## 🧪 Modelos probados

Se evaluaron varios modelos de boosting:

- ✅ **CatBoost** (mejor equilibrio entre recall y precisión)
- ✅ **XGBoost** (mayor recall sin umbral ajustado)
- ✅ **LightGBM** (buena velocidad y rendimiento)
- ✅ **VotingClassifier** (mejor resultado combinado)

### 🔎 Mejor combinación (Voting XGB + CatBoost):
- Precision: 0.36
- Recall: 0.51
- F1-score: 0.42
- ROC AUC: 0.86

---

## 🚀 Despliegue de la App

### 1. Requisitos

Instala las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

```bash
streamlit run app.py
```

La app se abrirá automáticamente en tu navegador.

---

## 📊 Dataset

- **Fuente**: Kaggle - [Give Me Some Credit Dataset](https://www.kaggle.com/c/GiveMeSomeCredit)
- **Observaciones**: 150.000 clientes con información financiera
- **Variable objetivo**: Impago2Años Nombre original:`SeriousDlqin2yrs` → indica si el cliente tuvo impagos en los próximos 2 años

---

## 🧠 ¿Qué incluye este proyecto?

- Limpieza avanzada de datos con clase personalizada (`LimpiezaBasica`)
- Preprocesamiento: winsorización + escalado robusto + SMOTE
- Comparación de modelos Boosting y VotingClassifier
- Optimización de hiperparámetros con Optuna
- Ajuste del umbral de decisión
- Aplicación de predicción con Streamlit

---

## 📌 Estado actual

✔️ Proyecto finalizado y funcional. Preparado para ser desplegado y presentado como parte de un portfolio profesional.

---

## 📧 Autora

**Raquel Vadillo** – Data Analyst / ML Enthusiast  
✉️ Contacto: rvad.datascient@gmail.com 
🔗 LinkedIn: 
