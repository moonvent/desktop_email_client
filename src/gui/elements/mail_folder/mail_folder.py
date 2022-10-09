import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout

from src.gui.config import STANDART_MAIL_FOLDER_WIDTH, STANDART_MAIL_FOLDER_HEIGHT
from src.gui.elements.mail_folder.bottom_row import BottomRow
from src.gui.elements.mail_folder.top_row import TopRow
from src.gui.elements.standart_layout import StandartLayout
from src.gui import styles
from src.gui import config


class MailFolder(StandartLayout):
    """
        Папка почты
    """

    def __init__(self,
                 parent,
                 **kwargs):
        """
        :param parent:
        :param kwargs: данные о письме: время полчение, тема, сообщение, статус просмотренно, количество непрочитанных
        """
        self.title = kwargs['title']
        self.seen_status = kwargs['seen_status']
        self.last_get_time = kwargs['last_get_time']
        self.message_text = kwargs['message_text']
        self.amount_not_reed = kwargs['amount_not_reed']

        super().__init__()
        self.setParent(parent)

    def load_ui(self):
        self.setObjectName(styles.MAIL_FOLDER_ID)
        self.setLayout(QVBoxLayout(self))

        layout = self.layout()
        layout.setContentsMargins(config.LEFT_MARGIN_MAIL_FOLDER, 0, 0, 0)
        layout.setSpacing(0)

        self.first_row_layout = TopRow(title=self.title,
                                       seen_status=self.seen_status,
                                       last_get_date=self.last_get_time,
                                       parent=self)
        self.second_row_layout = BottomRow(last_message_text=self.message_text,
                                           notification_number=self.amount_not_reed,
                                           parent=self)

        self.setFixedWidth(STANDART_MAIL_FOLDER_WIDTH)
        self.setFixedHeight(STANDART_MAIL_FOLDER_HEIGHT)

        layout.addWidget(self.first_row_layout)
        layout.addWidget(self.second_row_layout)
