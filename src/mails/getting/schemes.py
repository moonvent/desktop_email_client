from pydantic import BaseModel, Field


class FolderStatus(BaseModel):
    """
        Объект для лучшей обработки статуса папки
    """

    messages_amount: int = Field(gt=-1, description='Количество сообщений в папке', alias='MESSAGES')
    unseen_amount: int = Field(gt=-1, description='Количество непрочитанных в папке', alias='UNSEEN')
