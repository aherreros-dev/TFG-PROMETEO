from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt


class BasePage(QWidget):
    def __init__(self, title: str, description: str):
        super().__init__()
        self._build_ui(title, description)

    def _build_ui(self, title: str, description: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(12)

        lbl_title = QLabel(title)
        lbl_title.setObjectName("page_title")

        lbl_desc = QLabel(description)
        lbl_desc.setObjectName("page_description")

        card = QFrame()
        card.setObjectName("placeholder_card")
        card_layout = QVBoxLayout(card)
        placeholder = QLabel("— Contenido pendiente de implementación —")
        placeholder.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(placeholder)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_desc)
        layout.addSpacing(16)
        layout.addWidget(card)
        layout.addStretch()
