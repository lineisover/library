# Library 
Учебный проект по разработке сайта каталога книг на Django. 

## Содержание 
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Дополнительно](#дополнительно)

## Технологии 
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/) 
- [Boostrap](https://getbootstrap.com/)

## Начало работы 
### Склонируйте репозиторий:
```sh
& git clone https://github.com/lineisover/library
```
### Преходим в папку проекта:
```sh
& cd library
```
### Установить виртуальное окружение:
```sh
& py -3.11 -m venv .venv
```
`-3.11` - версия python  
`.venv` - путь к виртуальному окружению  

### Активировать виртуальное окружение:  
- Для Windows
```sh
& .venv\Scripts\activate.ps1
```
- Для Linux и MacOS
```sh
& source venv/bin/activate
```
### Устанавливаем зависимости:
```sh
& pip install -r requirements.txt
```
### Запускаем проект:
```sh
& python library\manage.py runserver
```
Profit!!!  
По умолчанию сервер будет запущен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)

## Дополнительно
### Запрос для добавления новой книги
`127.0.0.1:8000/add?name=new_book&author=new_author&year=new_year&genre=new_genre`  
Если книга с таким названием и тем же автором существует, то она не добавится.
##
### Фильтры книг
Фильтры могут быть:
- name - название книги
- author - автор книги
- year - год выпуска книги
- genre - жанр книги

пример строки:
`http://127.0.0.1:8000/filter/genre?param=антиутопия`
где 'genre' тип фильтра, а 'антиутопия' параметр запроса для фильтрации.