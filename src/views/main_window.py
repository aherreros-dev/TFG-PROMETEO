import os

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QFrame, QStackedWidget,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

from .pages.load_page import LoadPage
from .pages.preprocess_page import PreprocessPage
from .pages.model_page import ModelPage
from .pages.config_page import ConfigPage
from .pages.optimize_page import OptimizePage
from .pages.train_page import TrainPage
from .pages.validate_page import ValidatePage
from .pages.infer_page import InferPage

NAV_ITEMS = [
    ("01  CARGA DE DATOS",      LoadPage),
    ("02  PREPROCESAMIENTO",    PreprocessPage),
    ("03  SELECCIÓN DE MODELO", ModelPage),
    ("04  CONFIGURACIÓN",       ConfigPage),
    ("05  OPTIMIZACIÓN",        OptimizePage),
    ("06  ENTRENAMIENTO",       TrainPage),
    ("07  VALIDACIÓN",          ValidatePage),
    ("08  INFERENCIA",          InferPage),
]


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self._controller = controller
        self._nav_buttons: list[QPushButton] = []
        self._build_ui()
        self._navigate(0)

    def _build_ui(self):
        self.setWindowTitle("PROMETEO")
        self.setMinimumSize(1100, 680)

        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        root_layout.addWidget(self._build_sidebar())
        root_layout.addWidget(self._build_content(), stretch=1)

        self.setCentralWidget(root)

    def _build_sidebar(self) -> QWidget:
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Logo + título en fila
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(16, 20, 16, 4)
        header_layout.setSpacing(10)

        logo_label = QLabel()
        logo_path = os.path.join(ASSETS_DIR, "logo.png")
        pixmap = QPixmap(logo_path).scaled(44, 44, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(44, 44)

        text_block = QWidget()
        text_layout = QVBoxLayout(text_block)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(2)

        title = QLabel("PROMETEO")
        title.setObjectName("app_title")
        subtitle = QLabel("PREDICCIÓN DE INCENDIOS")
        subtitle.setObjectName("app_subtitle")

        text_layout.addWidget(title)
        text_layout.addWidget(subtitle)

        header_layout.addWidget(logo_label)
        header_layout.addWidget(text_block)

        layout.addWidget(header)

        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFixedHeight(1)
        layout.addWidget(sep)
        layout.addSpacing(8)

        for idx, (label, _) in enumerate(NAV_ITEMS):
            btn = QPushButton(label)
            btn.setObjectName("nav_btn")
            btn.setCheckable(False)
            btn.clicked.connect(lambda _, i=idx: self._navigate(i))
            self._nav_buttons.append(btn)
            layout.addWidget(btn)

        layout.addStretch()

        status = QLabel("v0.1.0  ·  TFG UEMC 2025")
        status.setObjectName("status_bar")
        status.setAlignment(Qt.AlignCenter)
        layout.addWidget(status)

        return sidebar

    def _build_content(self) -> QWidget:
        self._stack = QStackedWidget()
        self._stack.setObjectName("content_area")

        for _, PageClass in NAV_ITEMS:
            self._stack.addWidget(PageClass())

        return self._stack

    def _navigate(self, index: int):
        for i, btn in enumerate(self._nav_buttons):
            btn.setProperty("active", i == index)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

        self._stack.setCurrentIndex(index)
