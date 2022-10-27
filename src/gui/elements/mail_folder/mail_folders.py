import datetime

from PySide6.QtWidgets import QVBoxLayout, QPushButton

from src.gui.elements.mail_folder.mail_folder import MailFolder
from src.gui.elements.standart_layout import StandartLayout
from src.services.database import accounts as db_accounts


class MailForlders(StandartLayout):
    """
        Меню с *папками* почт (как чаты в ТГ)
    """

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

    def load_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.create_folders()

    def generate_folder(self, account: db_accounts.Accounts):
        return MailFolder(parent=self,
                          title='Title',
                          seen_status=1,
                          last_get_time=datetime.datetime.now(),
                          message_text='message_text',
                          amount_not_reed=23)

    def create_folders(self):
        layout = self.layout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        for account in db_accounts.get_accounts():
            folder = self.generate_folder(account=account)
            layout.addWidget(folder)
