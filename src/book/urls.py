# coding: utf-8
from django.conf.urls import url
from book.views import GenreList, GenreView, BookList, BookView


urlpatterns = [
    # url(r'^random/$', random_book, name='random_world'),
    url(r'^genre/$', GenreList.as_view(), name='book_genres'),
    url(r'^genre/(?P<slug>[\w-]+)/$', GenreView.as_view(), name='book_genre'),
    url(r'^book/$', BookList.as_view(), name='books'),
    url(r'^book/(?P<slug>[\w-]+)/$', BookView.as_view(), name='book'),
]
