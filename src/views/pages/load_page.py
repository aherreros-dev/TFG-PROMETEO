from .base_page import BasePage


class LoadPage(BasePage):
    def __init__(self):
        super().__init__(
            title="CARGA DE DATOS",
            description="Importa el dataset CSV con las variables topoclimáticas.",
        )
