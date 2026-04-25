import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from PySide6.QtWidgets import QApplication

from views.style import STYLESHEET
from views.main_window import MainWindow
from controllers.main_controller import MainController


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PROMETEO")
    app.setStyleSheet(STYLESHEET)

    controller = MainController()
    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
