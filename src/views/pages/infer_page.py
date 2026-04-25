from .base_page import BasePage


class InferPage(BasePage):
    def __init__(self):
        super().__init__(
            title="INFERENCIA",
            description="Predicción de riesgo de incendio sobre nuevos datos topoclimáticos.",
        )
