"""
    Главный объект GUI
"""


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSplitter

from src.gui import config, styles
from src.gui.elements.mail_folder.mail_folders import MailForlders
from src.gui.elements.standart_layout import StandartLayout


class MainWindow(StandartLayout):
    _splitter: QSplitter = None

    def __init__(self):
        super().__init__()

    def load_ui(self):
        self.setFixedWidth(config.APP_WIDTH)
        self.setFixedHeight(config.APP_HEIGHT)
        self._splitter = QSplitter(Qt.Horizontal, parent=self)

        self.setStyleSheet(styles.APP_STYLES)

        self.mails_folders = MailForlders(parent=self.splitter)
        self.splitter.addWidget(self.mails_folders)

    @property
    def splitter(self):
        return self._splitter

