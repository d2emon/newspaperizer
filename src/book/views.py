from django.views.generic import ListView, DetailView
from book.models import BookGenre, Book


class GenreList(ListView):
    model = BookGenre


class GenreView(DetailView):
    model = BookGenre


class BookList(ListView):
    model = Book


class BookView(DetailView):
    model = Book
