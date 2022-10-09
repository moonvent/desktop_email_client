"""
    Объект для работы с разными почтами,
    для интерфейса расширения ввода почт (у каждой разные хосты, названия папок и т.д),
    но интерфейс вывод на UI будет один
"""
import os

from imap_tools import MailBox, FolderInfo
from src.services.logging.custom_logger import logger
from src.config import TEST_HOST, TEST_LOGIN, TEST_PASSWORD
from src.mails.getting.schemes import FolderStatus


class MailImapBasicObject:
    _mail_object: MailBox = None
    _folders: tuple[FolderInfo] = None

    @property
    def mail(self):
        return self._mail_object

    @mail.setter
    def mail(self, value):
        self._mail_object = value

    @property
    def folders(self):
        return self._folders

    @folders.setter
    def folders(self, value):
        self._folders = value

    def __init__(self,
                 host: str,
                 login: str,
                 password: str):
        self._create_mail_object(host=host,
                                 login=login,
                                 password=password)

    def _create_mail_object(self,
                            host: str,
                            login: str,
                            password: str):
        try:
            self.mail = MailBox(host).login(login, password)

        except:
            logger.exception('Ошибка при авторизации')

        else:
            logger.debug(f'Успешно авторизировался с данными {TEST_HOST, TEST_LOGIN, TEST_PASSWORD}')

    # def __del__(self):
    #     self.mail.logout()

    def get_folders(self):
        self.folders = self.mail.folder.list()

    def get_folder_status(self, folder_name: str | FolderInfo = None) -> FolderStatus:
        """
            Получение информации о папке
        :param folder_name: название, или объект папки, если None, то возвращаем статус установленной сейчас папки
        :return: Объект FolderStatus, содержащий информацию о кол-ве сообщений и кол-ве непрочитанных сообщений
        """
        if folder_name:
            current_folder_name: str = self.mail.folder.get()

            if isinstance(folder_name, str):
                self.mail.folder.set(folder_name)

            elif isinstance(folder_name, FolderInfo):
                self.mail.folder.set(folder_name.name)

            folder_status = FolderStatus(**self.mail.folder.status())

            self.mail.folder.set(current_folder_name)

        else:
            folder_status = FolderStatus(**self.mail.folder.status())

        return folder_status

    def get_all_folders_status(self) -> tuple[FolderStatus]:
        """
            Получение всех статусов папок, если есть в этом необходимость
        :return: кортеж с объектами FolderStatus
        """
        folders_statuses = []

        for folder in self.folders:
            folders_statuses.append(self.get_folder_status(folder))

        return tuple(folders_statuses)

    def get_messages(self):
        ...


if __name__ == '__main__':
    mail_object = MailImapBasicObject(host=TEST_HOST,
                                      login=TEST_LOGIN,
                                      password=TEST_PASSWORD)
    print(mail_object.get_folder_status())
