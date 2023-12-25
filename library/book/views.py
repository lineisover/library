from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Author, Book

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
            'Фильтрация по {0} невозможна, существуют фильтры: {1}'.format(filter, *FILTER_LIST)
        )
    filter_elem = {filter: param}
    books_with_param = list(Book.objects.filter(**filter_elem))
    print(books_with_param)
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
