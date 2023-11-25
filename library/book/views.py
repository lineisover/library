from django.http import HttpResponseRedirect
from django.shortcuts import render

books = [{'id': 0,
          'name': 'Test',
          'author': 'test'},
         {'id': 1,
          'name': 'Test2',
          'author': 'test2'}]

last_id = 1


def index(request):
    return render(request, 'library/index.html', {'books': books})


def book(request):
    id = request.GET.get('id', '-1')
    name = request.GET.get('name', 'None')
    author = request.GET.get('author', 'None')
    return render(request, 'book/book.html', {'id': id, 'name': name, 'author': author})


def add_book(request):
    global last_id
    add_flag = request.GET.get('add', '0')
    if add_flag == '1':
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
