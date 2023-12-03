from django.db import models
from django.utils import timezone


class Book(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    title = models.CharField(verbose_name='Название',
                             help_text='Название книги до 100 символов',
                             max_length=100)
    author = models.CharField(verbose_name='Автор',
                              help_text='Автор книги до 100 символов',
                              max_length=100)
    year = models.DecimalField(verbose_name='Год издания',
                               help_text='Год издания книги',
                               max_digits=4,
                               decimal_places=0,
                               blank=False)
    genre = models.CharField(verbose_name='Жанр',
                             help_text='Жанр книги до 50 символов',
                             max_length=50,
                             blank=False)
    cover = models.CharField(verbose_name='Обложка',
                             max_length=250,
                             default='/img/no_photo.webp')
    publish = models.DateTimeField(verbose_name='Дата публикации',
                                   default=timezone.now)
    created = models.DateTimeField(verbose_name='Дата создания',
                                   auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения',
                                   auto_now=True)
    status = models.CharField(verbose_name='Статус',
                              max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        ordering = ['id']
        verbose_name = 'книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
