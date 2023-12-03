from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'year', 'publish', 'status']
    list_display_links = ['id', 'title']
    list_filter = ['status', 'author', 'year']
    search_fields = ['title', 'author']
