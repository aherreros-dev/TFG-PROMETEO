<p align="center">
  <img src="assets/logo.png" alt="PROMETEO Logo" width="160"/>
</p>

# PROMETEO
## Predictive Risk Observation & Machine learning Engine for Topoclimatic Emergency Operations

### Motor Topoclimático de Predicción de Incendios

**Trabajo de Fin de Grado · Universidad Europea Miguel de Cervantes (UEMC)**
Autor: Alejandro Herreros Rueda

---

## Descripción

PROMETEO es una herramienta de predicción de incendios forestales desarrollada como Trabajo de Fin de Grado. El sistema aplica algoritmos de **minería de datos y aprendizaje automático** sobre variables topoclimáticas (temperatura, humedad, viento, orografía del terreno, etc.) para estimar el riesgo de incendio en una zona determinada.

El nombre hace referencia al titán de la mitología griega que robó el fuego para entregárselo a los humanos — aquí el objetivo es anticiparse al fuego antes de que ocurra.

## Tecnologías principales

| Área | Herramienta |
|---|---|
| Lenguaje | Python 3.10 |
| Interfaz gráfica | PySide6 (Qt) |
| Machine Learning | scikit-learn |
| Optimización de hiperparámetros | Optuna |
| Explicabilidad del modelo | SHAP |
| Análisis y visualización | pandas, numpy, matplotlib, seaborn |
| Serialización de modelos | joblib |
| Gestión de entorno | conda |

## Estructura del proyecto

```
PROMETEO/
├── src/           # Código fuente principal
│   └── main.py   # Punto de entrada de la aplicación
├── data/          # Datasets (no versionados)
├── models/        # Modelos entrenados (no versionados)
└── requirements.txt  # Entorno conda
```

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/aherreros-dev/TFG-PROMETEO.git
cd TFG-PROMETEO

# Crear el entorno conda
conda env create -f requirements.txt
conda activate prometeo_env

# Ejecutar la aplicación
python src/main.py
```

## Estado del proyecto

El proyecto se encuentra en desarrollo activo como parte del TFG. Las funcionalidades se irán añadiendo de forma incremental a lo largo del curso.
