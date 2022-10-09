import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QHBoxLayout, QCheckBox, QSizePolicy

from src.gui.elements.standart_layout import StandartLayout

from src.services.gui.elements.mail_folder import top_row as util_top_row
from src.gui.config import STANDART_MAIL_FOLDER_ROW_HEIGHT


class TopRow(StandartLayout):

    title_label: QLabel = None
    seen_status_check_box: QCheckBox = None
    last_getting_date_label: QLabel = None

    def __init__(self,
                 title: str,
                 seen_status: bool,
                 last_get_date: datetime.datetime,
                 parent: StandartLayout):

        self.title = title
        self.seen_status = seen_status
        self.last_get_date = last_get_date
        super().__init__()
        self.setParent(parent)

    def load_ui(self):
        layout = QHBoxLayout(self)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.create_title_label()
        self.create_seen_status()
        self.create_last_get_date()

    def create_title_label(self):
        self.title_label = QLabel(parent=self)
        self.title_label.setText(self.title)
        self.title_label.setSizePolicy(QSizePolicy.Expanding,
                                       QSizePolicy.Preferred)
        self.title_label.setFixedHeight(STANDART_MAIL_FOLDER_ROW_HEIGHT)
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.layout().addWidget(self.title_label)

    def create_seen_status(self):
        self.seen_status_check_box = QCheckBox(parent=self)
        self.seen_status_check_box.setChecked(self.seen_status)
        self.seen_status_check_box.setDisabled(True)
        self.layout().addWidget(self.seen_status_check_box)
        self.seen_status_check_box.setFixedWidth(30)

    def create_last_get_date(self):
        self.last_getting_date_label = QLabel(parent=self)
        self.last_getting_date_label.setText(util_top_row.generate_ouput_time(self.last_get_date))
        self.last_getting_date_label.setSizePolicy(QSizePolicy.Fixed,
                                                   QSizePolicy.Fixed)
        self.layout().addWidget(self.last_getting_date_label)
