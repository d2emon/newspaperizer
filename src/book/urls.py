# coding: utf-8
from django.conf.urls import url
from book.views import random_book, GenreListView, WikiListView, GenreView, BookListView, BookView


urlpatterns = [
    url(r'^$', GenreListView.as_view()),

    url(r'^genre/$', GenreListView.as_view(), name='book_genres'),
    url(r'^orphans/$', GenreView.as_view(), name='book_genres_orphans'),

    url(r'^genre/(?P<slug>[\w-]+)/$', GenreView.as_view(), name='book_genre'),

    url(r'^genre/__page.opt$', WikiListView.as_view(), name='book_genres_wiki'),
    url(r'^genre/(?P<slug>[\w-]+)/__page.opt$', WikiListView.as_view(), name='book_genre_wiki'),

    url(r'^random/(?P<genre>[\w-]+)?/?$', random_book, name='random_book'),
    url(r'^book/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<slug>[\w-]+)/$', BookView.as_view(), name='book'),

]
