import datetime

from PySide6.QtWidgets import QVBoxLayout, QPushButton

from src.gui.elements.mail_folder.mail_folder import MailFolder
from src.gui.elements.standart_layout import StandartLayout


class MailForlders(StandartLayout):
    """
        Меню с *папками* почт (как чаты в ТГ)
    """

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

    def load_ui(self):
        layout = QVBoxLayout(parent=self)
        self.setLayout(layout)
        self.create_plug_buttons()

    def create_plug_buttons(self):
        layout = self.layout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        for i in range(5):
            dummy_button = MailFolder(parent=self,
                                      title='Title',
                                      seen_status=1,
                                      last_get_time=datetime.datetime.now(),
                                      message_text='message_text',
                                      amount_not_reed=23)
            # dummy_button = QPushButton(self)
            # dummy_button.setText('sex')
            layout.addWidget(dummy_button)
