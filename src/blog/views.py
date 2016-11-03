from django.views.generic import ListView, DetailView
from blog.models import News


class NewsListView(ListView):
    model = News
    
    
class NewsView(DetailView):
    model = News