from django.views.generic import ListView, DetailView
from newspaper.models import Newspaper


class NewspaperListView(ListView):
    model = Newspaper
    
    
class NewspaperDetailView(DetailView):
    model = Newspaper