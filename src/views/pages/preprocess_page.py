from .base_page import BasePage


class PreprocessPage(BasePage):
    def __init__(self):
        super().__init__(
            title="PREPROCESAMIENTO",
            description="Limpieza, normalización y transformación de variables.",
        )
