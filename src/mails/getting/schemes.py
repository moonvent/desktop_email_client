from pydantic import BaseModel, Field


class FolderStatus(BaseModel):
    """
        Объект для лучшей обработки статуса папки
    """

    messages_amount: int = Field(gt=-1, description='Количество сообщений в папке', alias='MESSAGES')
    unseen_amount: int = Field(gt=-1, description='Количество непрочитанных в папке', alias='UNSEEN')


class MailServers(BaseModel):
    imap_host: str = Field(description='хост IMAP сервера')
    imap_port: int = Field(gt=0, description='порт IMAP сервера', default=993)
    smtp_host: str = Field(description='SMTP сервер почтовый')
    smtp_port: int = Field(gt=0, description='SMTP сервер почтовый', default=465)
