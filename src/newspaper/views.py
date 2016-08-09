from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from newspaper.models import Newspaper


def index(request):
    return HttpResponse("Hello world!")
    
class NewspaperListView(ListView):
    model = Newspaper
    
    
class NewspaperDetailView(DetailView):
    model = Newspaper