from .base_page import BasePage


class TrainPage(BasePage):
    def __init__(self):
        super().__init__(
            title="ENTRENAMIENTO",
            description="Entrenamiento asíncrono del modelo (QThread). Monitorización en tiempo real.",
        )
