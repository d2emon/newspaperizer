from django.views.generic import ListView, DetailView
from book.models import BookGenre


class GenreList(ListView):
    model = BookGenre


class GenreView(DetailView):
    model = BookGenre
