import sys

from PySide6.QtWidgets import QApplication

from src.gui.config import APP
from src.gui.main_window import MainWindow


def start_app():
    widget = MainWindow()
    widget.show()
    sys.exit(APP.exec())
