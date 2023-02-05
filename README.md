# **REST API для Yatube**
REST API для Yatube, с помощью которого можно передавать данные в любое приложение или на фронтенд

## Установка
Для того, чтобы развернуть проект на локальной машине, необходимо
* клонировать репозиторий 
 ```
 git clone https://github.com/ekhitalenko/api_final_yatube
 ```
* перейти в папку проекта 
 ```
 cd api_final_yatube
 ```
* создать виртульное окружение:
  * ```для Windows```:
   ```
   python -m venv venv
   ```
  * ```для Linux и macOS```: 
  ```
   python3 -m venv venv
   ```
* активировать виртульное окружение 
  * ```для Windows```:
   ```
   source venv/Scripts/activate
   ```
  * ```для Linux и macOS```: 
  ```
   source venv/bin/activate
   ```
* установить все необходимые пакеты
  ```
   pip install -r requirements.txt
   ```
* выполнить миграции 
  * ```для Windows```:
   ```
   python manage.py migrate
   ```
  * ```для Linux и macOS```: 
  ```
   python3 manage.py migrate
   ```
* запустить проект 
  * ```для Windows```:
   ```
   python manage.py runserver
   ```
  * ```для Linux и macOS```: 
  ```
   python3 manage.py runserver
   ```
## Примеры запросов к API

```Зарегистрировать нового пользователя```
```
http://127.0.0.1:8000/api/v1/users/
request POST, 
body '{
    "username": 
        "yourusername",
    "password": 
        "yourpassword"
}'
```
```Создать JWT-токена```
```
http://127.0.0.1:8000/api/v1/jwt/create/
request POST, 
body '{
    "username": 
        "yourusername",
    "password": 
        "yourpassword"
}'
```
```Получить список постов```
```
http://127.0.0.1:8000/api/v1/posts/
request GET, 
header 'Authorization: Bearer yourtoken'
```
```Создать новый пост```
```
http://127.0.0.1:8000/api/v1/posts/
request POST,
header 'Authorization: Bearer yourtoken'
body '{
    "text": "Текст поста"
}'
```
```Создать новый комментарий```
```
http://127.0.0.1:8000/api/v1/posts/post-id/comments/
request POST,
header 'Authorization: Bearer yourtoken'
body '{
    "text": "Текст комментария"
}'
```
