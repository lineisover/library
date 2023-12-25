from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'cover', 'cover_display', 'genre', 'year', 'publish', 'updated', 'status']
    readonly_fields = ['cover_display', 'publish', 'updated']
    list_display = ['id', 'title', 'cover_display', 'author', 'genre', 'year', 'publish', 'updated', 'status']
    list_display_links = ['id', 'author', 'title']
    list_filter = ['status', 'author', 'year']
    search_fields = ['title']

    @admin.display(description='Обложка')
    def cover_display(self, book: Book):
        if book.cover:
            return mark_safe(
                f"<img src='{book.cover.url}' width=100><br><a href='{book.cover.url}'>{book.cover.url}</a>"
            )
        else:
            return 'Нет обложки'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
