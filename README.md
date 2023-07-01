# **REST API для Yatube**
REST API для Yatube, с помощью которого можно передавать данные в любое приложение или на фронтенд

<details>
   <summary>Запуск проекта локально</summary> 
 
Клонировать репозиторий и перейти в него в командной строке:
 ```
 git clone git@github.com:kkhitalenko/Yatube_API.git
 ```
 ```
 cd Yatube_API/
 ```
Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd yatube_api/
```
```
python manage.py migrate
```
Запустить проект:

```
python manage.py runserver
```
</details>

Документация  и примеры запросов доступны после запуска проекта по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Используемые технологиии:

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg" title="SQLite" alt="SQLite" width="40" height="40"/>&nbsp;
</div>