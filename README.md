# Проект "Мой личный Email клиент"

---

## Окружение

Проект написан на `Python 3.10` , с зависимостями:

* [pipenv](https://pypi.org/project/pipenv/) (пакетный менеджер);
* [PySide6](https://pypi.org/project/PySide6/) (gui);
* [envelope](https://pypi.org/project/loguru/) (работа с smtp);
* [imap-tools](https://pypi.org/project/imap-tools/) (работа с imap);
* [sphinx](https://pypi.org/project/Sphinx/) (генерация документации);
* *список может дополняться*

Все зависимости с версиями указаны в файле `pipfile` но могут быть и дополнительно указаны в ```requirements.txt``` 

---

## Файловая иерархия


Стартовый файл в корневой директории и называется `main.py`

Документации документация к коду находится в файле `/docs/_build/html/index.html`

Тесты находятся в директории `tests`, файл для запуска всех тестов `tests/start_all_tests.py` 

---

## Установка проекта с виртуальным окружением на Linux

#### Создание виртуального окружения
`python3.10 -m venv venv`

#### Активация виртуального окружения
`venv/bin/active`

#### Установка зависимостей 
`pip install -r requirements.txt` и `pipenv install`, или `pip install -r requirements.txt`

#### Запуск проекта
`python main.py`

#### Запуск тестов
`python tests/start_all_tests.py`

## Планы на будущее 

- [ ] Добавить [кнопки](https://shields.io/) о зависимостях в readme;
- [ ] Настроить корректно и красиво документацию;
- [ ] Сделать автоустановку проекта (для Windows, Mac и Linux);
- [ ] Сделать авторазвертку проекта через `setup.py`;
- [ ] Настроить или установить лицензию;
- [ ] Залить проект в PyPI;
