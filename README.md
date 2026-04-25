<p align="center">
  <img src="assets/logo.png" alt="PROMETEO Logo" width="160"/>
</p>

<h1 align="center">PROMETEO</h1>
<h3 align="center">Predictive Risk Observation & Machine learning Engine for Topoclimatic Emergency Operations</h3>
<p align="center"><em>Motor Topoclimático de Predicción de Incendios Forestales</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySide6-Qt-41CD52?style=flat-square&logo=qt&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikitlearn&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-gradient%20boosting-E84F1C?style=flat-square"/>
  <img src="https://img.shields.io/badge/Optuna-bayesian%20opt-6C63FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/SHAP-explainability-FF5500?style=flat-square"/>
  <img src="https://img.shields.io/badge/conda-environment-44A833?style=flat-square&logo=anaconda&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square"/>
</p>

<p align="center">
  <strong>Trabajo de Fin de Grado · Universidad Europea Miguel de Cervantes (UEMC)</strong><br/>
  Alejandro Herreros Rueda · 2026
</p>

---

## Descripción

PROMETEO es una aplicación de escritorio para la predicción de incendios forestales. El sistema aplica algoritmos de **minería de datos y aprendizaje automático** sobre variables topoclimáticas (temperatura, humedad, viento, orografía del terreno, etc.) para estimar el riesgo de incendio en una zona determinada.

El modelo final es un **SVM con kernel RBF** optimizado mediante búsqueda bayesiana (Optuna), priorizando la sensibilidad (Recall ≥ 86%) para minimizar los falsos negativos — un incendio no detectado es siempre más grave que una falsa alarma.

El nombre hace referencia al titán de la mitología griega que robó el fuego para entregárselo a los humanos — aquí el objetivo es anticiparse al fuego antes de que ocurra.

---

## Stack tecnológico

| Área | Herramienta |
|---|---|
| Lenguaje | Python 3.10 |
| Interfaz gráfica | PySide6 (Qt) — QThread para entrenamiento asíncrono |
| Machine Learning | scikit-learn, XGBoost |
| Optimización de hiperparámetros | Optuna (Bayesian Optimization) |
| Explicabilidad (XAI) | SHAP + Test de Permutación |
| Análisis y visualización | pandas, numpy, matplotlib, seaborn |
| Serialización de modelos | joblib |
| Gestión de entorno | conda |

---

## Estructura del proyecto

```
PROMETEO/
├── assets/                  # Logo e imágenes
├── src/
│   ├── main.py              # Punto de entrada
│   ├── models/              # Capa de datos y estado (MVC)
│   ├── views/               # Interfaz gráfica — PySide6
│   │   ├── pages/           # 8 vistas (una por caso de uso)
│   │   └── style.py         # Tema visual global
│   └── controllers/         # Lógica y mediación M↔V
├── data/                    # Datasets (no versionados)
├── models/                  # Modelos entrenados (no versionados)
├── environment.yml          # Entorno conda
└── requirements.txt         # Dependencias pip
```

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/aherreros-dev/TFG-PROMETEO.git
cd TFG-PROMETEO

# Crear y activar el entorno conda
conda env create -f environment.yml
conda activate prometeo_env

# Ejecutar la aplicación
python src/main.py
```

---

## Estado del proyecto

El proyecto se encuentra en **desarrollo activo**. Las funcionalidades se implementan de forma incremental siguiendo los 8 casos de uso definidos en el DER.

| # | Módulo | Estado |
|---|---|---|
| 01 | Carga de datos (CSV) | 🔲 Pendiente |
| 02 | Preprocesamiento | 🔲 Pendiente |
| 03 | Selección de modelo | 🔲 Pendiente |
| 04 | Configuración de hiperparámetros | 🔲 Pendiente |
| 05 | Optimización (Optuna) | 🔲 Pendiente |
| 06 | Entrenamiento asíncrono | 🔲 Pendiente |
| 07 | Validación y métricas | 🔲 Pendiente |
| 08 | Inferencia | 🔲 Pendiente |
