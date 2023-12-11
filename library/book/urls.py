from django.urls import path, re_path
from . import views


urlpatterns = [
    path('allfilters/', views.all_filters, name='all_filters'),
    # path('add/', views.add_book, name='add'),
    path('author/<slug:slug_author>/', views.author, name='author'),
    path('book/<int:id>/', views.book, name='book'),
    re_path(r'^filter/(?P<filter>\S+)', views.filter, name='filter'),
    path('', views.index, name='home'),
]
