from django.views.generic import ListView, DetailView
from book.models import BookGenre, ScienceBook
from django.shortcuts import redirect


class GenreListView(ListView):
    model = BookGenre


class WikiListView(ListView):
    model = BookGenre
    template_name = 'book/wiki_list.html'


class GenreView(DetailView):
    model = BookGenre


def random_book(request):
    book = ScienceBook.objects.order_by('?').first()
    return redirect(book.get_absolute_url())


class BookListView(ListView):
    model = ScienceBook


class BookView(DetailView):
    model = ScienceBook
