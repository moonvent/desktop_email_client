from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from src.database.config import ACCOUNTS_TABLE_NAME, MAILS_TABLE_NAME, SQLITE_ENGINE_URL

engine = create_engine(SQLITE_ENGINE_URL)
Base = declarative_base()


class Mails(Base):
    __tablename__ = MAILS_TABLE_NAME

    id = Column(Integer, primary_key=True)
    smtp_host = Column(String(50), comment='smtp host')
    smtp_port = Column(SmallInteger, comment='smtp port')
    imap_host = Column(String(50), comment='imap host')
    imap_port = Column(SmallInteger, comment='imap port')


class Accounts(Base):
    __tablename__ = ACCOUNTS_TABLE_NAME

    id = Column(Integer, primary_key=True)
    email = Column(String(50),
                   comment='Емейл адрес пользователя')
    password = Column(String(1024),
                      comment='Пароль пользователя')
    mail = Column(Integer, ForeignKey(f'{MAILS_TABLE_NAME}.id'))
