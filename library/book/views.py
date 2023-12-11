from django.forms import model_to_dict
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from .models import Author, Book

# books = [{'id': 0,
#           'name': '1984',
#           'author': 'Джордж Оруэлл',
#           'year': '1949',
#           'genre': 'антиутопия',
#           'cover': '/img/covers/0/1984.webp'},
#          {'id': 1,
#           'name': 'Скотный двор',
#           'author': 'Джордж Оруэлл',
#           'year': '1945',
#           'genre': 'антиутопия',
#           'cover': '/img/covers/1/123.jpg'},
#          {'id': 2,
#           'name': 'Глотнуть воздуха',
#           'author': 'Джордж Оруэлл',
#           'year': '1939',
#           'genre': 'антиутопия',
#           'cover': '/img/no_photo.webp'},
#          {'id': 3,
#           'name': 'Дагон',
#           'author': 'Говард Лавкрафт',
#           'year': '1917',
#           'genre': 'ужасы',
#           'cover': '/img/no_photo.webp'},
#          {'id': 4,
#           'name': 'Картина в доме',
#           'author': 'Говард Лавкрафт',
#           'year': '1920',
#           'genre': 'ужасы',
#           'cover': '/img/no_photo.webp'},
#          {'id': 5,
#           'name': 'Из глубин мироздания',
#           'author': 'Говард Лавкрафт',
#           'year': '1920',
#           'genre': 'ужасы',
#           'cover': '/img/no_photo.webp'},
#          {'id': 6,
#           'name': 'Хоббит, или Туда и обратно',
#           'author': 'Джон Рональд Руэл Толкин',
#           'year': '1937',
#           'genre': 'фентези',
#           'cover': '/img/no_photo.webp'},
#          {'id': 7,
#           'name': 'Братство Кольца',
#           'author': 'Джон Рональд Руэл Толкин',
#           'year': '1954',
#           'genre': 'фентези',
#           'cover': '/img/no_photo.webp'},
#          {'id': 8,
#           'name': 'Две крепости',
#           'author': 'Джон Рональд Руэл Толкин',
#           'year': '1954',
#           'genre': 'фентези',
#           'cover': '/img/no_photo.webp'},
#          {'id': 9,
#           'name': 'Возвращение короля',
#           'author': 'Джон Рональд Руэл Толкин',
#           'year': '1955',
#           'genre': 'фентези',
#           'cover': '/img/no_photo.webp'}]

# last_id = 9
FILTER_LIST = ('title', 'author', 'year', 'genre')


def index(request):
    books = Book.published.all()
    return render(request, 'library/index.html', {'books': books})


def book(request, id):
    try:
        book = Book.objects.get(pk=id)
        return render(request, 'book/book.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponseNotFound('<h2>Книги с id: {0} не существует в библиотеке.</h2>'.format(id))


# TODO: Плохо сделаны исключения, надо разобраться.
def author(request, slug_author):
    try:
        author = get_object_or_404(Author, slug=slug_author)
        books = Book.published.filter(author=author.pk)
        return render(request, 'library/index.html', {'books': books})
    except Book.DoesNotExist:
        return HttpResponseNotFound('<h2>Книг автора: {0} не существует в библиотеке.</h2>'.format(author))


# TODO: Сделать обработку исключений
def filter(request, filter):
    global FILTER_LIST
    param = request.GET.get('param', '')
    if filter not in FILTER_LIST:
        return HttpResponseNotFound(
            'Фильтрация по {0} невозможна, существуют фильтры: {1}'.format(filter, *FILTER_LIST))
    filter_elem = {filter: param}
    books_with_param = list(Book.objects.filter(**filter_elem))
    print(books_with_param)
    # for book in list(Book.objects.filter(filter=param)):
    #     if book.get(filter) == param:
    #         books_with_param.append(book)
    # if len(books_with_param) == 0:
    #     return HttpResponseNotFound('Нет книг соответствующих запросу')
    # else:
    return render(request, 'library/index.html', {'books': books_with_param})


def all_filters(request):
    global FILTER_LIST
    list_filters = dict()
    for filter in FILTER_LIST[1:]:
        list_filters.setdefault(filter, [])
    books = list(Book.objects.values())
    for book in books:
        for filter in FILTER_LIST[1:]:
            if book.get(filter) not in list_filters.get(filter):
                list_filters[filter].append(book.get(filter))
    return render(request, 'library/filters.html', {'list_filters': list_filters})


# def add_book(request):
#     global last_id
#     name = request.GET.get('name', '')
#     author = request.GET.get('author', '')
#     year = request.GET.get('year', '')
#     genre = request.GET.get('genre', '')
#     if name and author and year and genre:
#         for el in books:
#             find_result = False
#             if name in el.get('name') and author in el.get('author'):
#                 find_result = True
#                 break
#         if not find_result:
#             books.append({'id': last_id + 1,
#                           'name': str(name),
#                           'author': author,
#                           'year': year,
#                           'genre': genre,
#                           'cover': '/img/no_photo.webp'})
#             last_id += 1
#     return HttpResponseRedirect('/')
