# PY_test_case_IBS
Тестовое задание для "ИНТЕРНЕТ-БИЗНЕС-СИСТЕМЫ" на языке python

Загруженное на хостинг:https://ibs.onrender.com/docs


# Реализованные метады
1. GET:/users - возращает всех пользователей
```
Параметры:
limit: Максимальное число пользователей при возрате 
offset: Смещение
orderBy: Сортировать по убыванию или возратснию (DESC/ASC)
OrderField: Поле по кторому будет проходить сортировка (id/name/username/job)
```
2. GET:/posts/{user_id} - возращает все посты пользователя с id = user_id
```
Параметры:
limit: Максимальное число пользователей при возрате 
offset: Смещение
orderBy: Сортировать по убыванию или возратснию (DESC/ASC)
OrderField: Поле по кторому будет проходить сортировка (id/title/description/date)
```
3. POST:/users - создаёт нового пользователя
```
Тело запроса:
{
  "name": str,
  "username": str,
  "job": str,
  "photo": str
}
```
4. POST:/posts - создает новый пост
```
Тело запроса:
{
  "id_user": int,
  "title": str,
  "description": str,
  "date": date
}
```
# Установка проекта
1. Сделать clone проекта (убедиться что в пути нет русских букв)
```
git clone https://github.com/Darling-Amk/PY_test_case_IBS.git
```
2. Перейти в папку с проектом
```
cd .\PY_test_case_IBS\
```
3. Создать и актирвировать виртуальное окружение
```
python -m venv ibs
```
```
.\ibs\Scripts\activate
```
4. Установить библиотеки из файла requirements.txt
```
pip install -r requirements.txt
```
5. При необходимости обновите pip
6. Подключаем и настраиваем алембик:
```
alembic init migration
```
7. В файле alembic.ini указываем адрес базы:
```
[alembic]
...
sqlalchemy.url = sqlite:///{Путь до папки с проектом}/ibs.db

Пример:
sqlalchemy.url = sqlite:////tmp/PY_test_case_IBS/ibs.db
```
8. В созданной папке migration изменяем файл env.py 
```
# Добавляем в начало
from src.models import metadata

...
# меняем None на metadata в 21 строке
target_metadata = metadata
```
9. Создаем первую миграцию(находясь в папке проекта)
```
alembic revision --autogenerate -m 'initial'
```

10. Применяем миграцию из папки versions (вставить нужно только название,без преписки \_initial.py)
```
alembic upgrade сгенерерованное_имя_миграции
```
11. Запускаем приложение
```
python main.py
```
12. Переходим по адрессу 
```
http://127.0.0.1:8000/docs
```
