from PySide6.QtWidgets import QWidget


class StandartLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self):
        """
            Установка начальных параметров виджета
        :return:
        """
        self._not_implemented()

    def _not_implemented(self):
        raise NotImplementedError(f'Не переопределен метод {self.load_ui.__name__} в классе {self.__class__.__name__}')
