"""
    Конфигурационный файл, установка констант, загрузка переменных окружений и т.д.
"""

import os
import sys
from pathlib import Path

PROJECT_NAME = 'Email client'
PROJECT_DESCRIPTION = 'Мой личный email клиент, так как я не нашел подходящего для себя'

VERSION = '0.0.1'
ENV_FILE = '.env'
WORK_DIR = 'desktop_email_client'


from dotenv import load_dotenv


def get_root_dir():
    current_dir = os.getcwd()
    path = Path(current_dir)
    while not str(path).endswith(WORK_DIR):
        path = path.parent
    os.chdir(path)
    return path


PROJECT_ROOT_DIR = get_root_dir()

load_dotenv(ENV_FILE)

LOG_FILE = 'logs.txt'

TEST_HOST = os.environ.get('TEST_HOST')
TEST_LOGIN = os.environ.get('TEST_LOGIN')
TEST_PASSWORD = os.environ.get('TEST_PASSWORD')

