# Project "Contacts"

## Задача

> Реализация RESTful API для работы с записной книгой.

## Описание

#### Нужно разработать простое API для работы с записной книгой, которое позволит:

* Добавлять новые контакты.
* Удалять контакты по идентификатору.
* Получать список всех контактов.
* Получать контакт по идентификатору.
* Обновлять контакт по идентификатору.

## Основные требования:

> Используйте Python 3.8+ и любой удобный вам фреймворк (например, Flask, FastAPI, Django).
> Для хранения данных используйте Postgres(развернутый в docker-compose).
> Реализуйте базовые обработчики ошибок (например, контакт не найден).
> Примените простую систему аутентификации (можно Basic Auth).

## Модель данных:

#### Контакт должен содержать следующую информацию:

* Идентификатор (ID)
* Имя Фамилия
* Телефон
* Электронная почта

## Дополнительные задачи:

> Добавьте возможность поиска контактов по имени или фамилии.
> Реализуйте пагинацию для списка контактов. Примените миграции для базы данных.

Основные технологии:
--------------------

```
* Python 3.11.1
* Django 4.2.4
* Django REST Framework 3.14.0
* Postgresql 14.5
```

```
* Docker
* docker-compose
```

Установка и запуск
------------------

* Переходим в директорию проекта

```cd contacts```

* Создаем файл .env такой же, как .env.sample (меняем настройки при необходимости)

```touch .env```

> > > Если в файле .env в переменной ENV_TYPE установить значение local, то проект будет запускаться с sqlite

##### Запуск локально или [запуск с помощью docker-compose](#docker)

###### Локально

* Создаем виртуальное окружение

```python3 -m venv venv```

* Активируем виртуальное окружение

```source venv/bin/activate```

* Устанавливаем зависимости

```pip install -r requirements.txt```

* Выполняем миграции

```python3 manage.py migrate```

* Запуск

```python3 manage.py runserver```


<a name="docker"></a> Запуск с помощью docker-compose
-------------------------------

###### docker-compose

##### Делаем файл docker_commands.sh исполняемым

```chmod +x docker_commands.sh```

##### Запуск

```docker-compose up --build```

##### API документация

[documentation](http://127.0.0.1:8000/docs)

