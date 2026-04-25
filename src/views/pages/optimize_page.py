from .base_page import BasePage


class OptimizePage(BasePage):
    def __init__(self):
        super().__init__(
            title="OPTIMIZACIÓN",
            description="Búsqueda automática de hiperparámetros con Optuna (Bayesian Optimization).",
        )
