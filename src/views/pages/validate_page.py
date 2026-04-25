from .base_page import BasePage


class ValidatePage(BasePage):
    def __init__(self):
        super().__init__(
            title="VALIDACIÓN",
            description="Métricas de evaluación: Recall, Precisión, F1, Matriz de Confusión, SHAP.",
        )
