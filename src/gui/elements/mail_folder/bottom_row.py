from PySide6.QtCore import Qt
from src.gui.config import STANDART_MAIL_FOLDER_ROW_HEIGHT
from PySide6.QtWidgets import QLabel, QHBoxLayout, QSizePolicy

from src.gui.elements.standart_layout import StandartLayout


class BottomRow(StandartLayout):

    last_message_text_label: QLabel = None
    notification_number_label: QLabel = None

    def __init__(self,
                 last_message_text: str,
                 notification_number: bool,
                 parent: StandartLayout):

        self.last_message_text = last_message_text
        self.notification_number = notification_number
        super().__init__()
        self.setParent(parent)

    def load_ui(self):
        layout = QHBoxLayout(self)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.create_last_message_text_label()
        self.create_notification_number_label()

    def create_last_message_text_label(self):
        self.last_message_text_label = QLabel(parent=self)
        self.last_message_text_label.setText(self.last_message_text)
        self.last_message_text_label.setSizePolicy(QSizePolicy.Expanding,
                                                   QSizePolicy.Preferred)
        self.last_message_text_label.setFixedHeight(STANDART_MAIL_FOLDER_ROW_HEIGHT)
        self.last_message_text_label.setAlignment(Qt.AlignLeft)
        self.layout().addWidget(self.last_message_text_label)

    def create_notification_number_label(self):
        self.notification_number_label = QLabel(parent=self)
        self.notification_number_label.setSizePolicy(QSizePolicy.Fixed,
                                                     QSizePolicy.Fixed)
        self.notification_number_label.setText(str(self.notification_number))
        self.layout().addWidget(self.notification_number_label)


