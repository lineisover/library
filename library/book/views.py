from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

books = [{'id': 0,
          'name': '1984',
          'author': 'Джордж Оруэлл'},
         {'id': 1,
          'name': 'Скотный двор',
          'author': 'Джордж Оруэлл'},
         {'id': 2,
          'name': 'Глотнуть воздуха',
          'author': 'Джордж Оруэлл'},
         {'id': 3,
          'name': 'Дагон',
          'author': 'Говард Лавкрафт'},
         {'id': 4,
          'name': 'Картина в доме',
          'author': 'Говард Лавкрафт'},
         {'id': 5,
          'name': 'Из глубин мироздания',
          'author': 'Говард Лавкрафт'},
         {'id': 6,
          'name': 'Хоббит, или Туда и обратно',
          'author': 'Джон Рональд Руэл Толкин'},
         {'id': 7,
          'name': 'Братство Кольца',
          'author': 'Джон Рональд Руэл Толкин'},
         {'id': 8,
          'name': 'Две крепости',
          'author': 'Джон Рональд Руэл Толкин'},
         {'id': 9,
          'name': 'Возвращение короля',
          'author': 'Джон Рональд Руэл Толкин'}]

last_id = 9


def index(request):
    return render(request, 'library/index.html', {'books': books})


def book(request, id):
    id = id
    book = None
    for el in books:
        if el.get('id') == int(id):
            book = el
    if book:
        return render(request, 'book/book.html', book)
    else:
        return HttpResponseNotFound('Книги с id: {0} не существует.'.format(id))


def add_book(request):
    global last_id
    name = request.GET.get('name', '')
    author = request.GET.get('author', '')
    if name and author:
        for el in books:
            find_result = False
            if name in el.get('name') and author in el.get('author'):
                find_result = True
                break
        if not find_result:
            books.append({'id': last_id + 1,
                          'name': str(name),
                          'author': author})
            last_id += 1
    return HttpResponseRedirect('/')
