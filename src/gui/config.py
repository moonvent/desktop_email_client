from PySide6.QtWidgets import QApplication


APP = QApplication()

SCREEN = APP.primaryScreen()

SCREEN_WIDTH = SCREEN.size().width()
HEIGHT_WIDTH = SCREEN.size().height()


APP_WIDTH = 1000
APP_HEIGHT = 563


STANDART_MAIL_FOLDER_WIDTH = int(APP_WIDTH * .2)
STANDART_MAIL_FOLDER_HEIGHT = 60
STANDART_MAIL_FOLDER_ROW_HEIGHT = int(STANDART_MAIL_FOLDER_HEIGHT / 2)


TODAY_TIME = '%H:%M'
LAST_WEEK_TIME = '%a'
LONG_AGO = '%d.%m.%Y'


LEFT_MARGIN_MAIL_FOLDER = 12
