# QRKot

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Practicum.Yandex](https://img.shields.io/badge/-Practicum.Yandex-464646?style=flat&logo=Practicum.Yandex&logoColor=56C0C0&color=008080)](https://practicum.yandex.ru/)

## Описание проекта
QRKot — это приложение для управления Благотворительным фондом. Фонд 
принимает пожертвования и распределяет их по благотворительным 
проектам.

## Развертывание проекта

1. Клонировать проект с *GitHub*.
2. Развернуть и активировать виртуальное окружение.
3. Создать файл `.env` по шаблону ниже:
    <details>
        <summary>.env</summary>

        APP_TITLE=<название приложения>
        APP_DESCRIPTION=Приложение для Благотворительного фонда
        DB_URL=sqlite+aiosqlite:///./<название БД>.db
        SECRET=
        TYPE=
        PROJECT_ID=
        PRIVATE_KEY_ID=
        PRIVATE_KEY=
        CLIENT_EMAIL=
        CLIENT_ID=
        AUTH_URI=
        TOKEN_URI=
        AUTH_PROVIDER_X509_CERT_URL=
        CLIENT_X509_CERT_URL=
        EMAIL=
   </details>
4. Установить зависимости из файла `requirements.txt`.
5. Применить миграции (см. *alembic/README.md*)
6. Запустить приложение: `uvicorn app.main:app`

## API проекта 

Документация: [Swagger](http://127.0.0.1:8000/docs)

## Авторы проекта

* Иван Сиснёв 
* Команда курса "Python-разработчик плюс" "Яндекс Практикум"