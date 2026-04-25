from models.app_model import AppModel


class MainController:
    """Mediates between views and the application model."""

    def __init__(self):
        self._model = AppModel()

    @property
    def model(self) -> AppModel:
        return self._model
