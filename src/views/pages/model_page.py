from .base_page import BasePage


class ModelPage(BasePage):
    def __init__(self):
        super().__init__(
            title="SELECCIÓN DE MODELO",
            description="Elige el algoritmo de clasificación (Strategy Pattern).",
        )
