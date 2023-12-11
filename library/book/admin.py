from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'year', 'publish', 'status']
    list_display_links = ['id', 'author', 'title']
    list_filter = ['status', 'author', 'year']
    search_fields = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
