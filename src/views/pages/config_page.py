from .base_page import BasePage


class ConfigPage(BasePage):
    def __init__(self):
        super().__init__(
            title="CONFIGURACIÓN",
            description="Ajuste manual de hiperparámetros del modelo seleccionado.",
        )
