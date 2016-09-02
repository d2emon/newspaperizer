from django.http import HttpResponse
from django.views.generic import ListView # , DetailView
from newspaper.models import Newspaper, Year


def index(request):
    return HttpResponse("Hello world!")

def years(request, pk):
    np = Newspaper.objects.get(pk=pk)
    issues = np.get_issues
    return HttpResponse(np)
    # dv = NewspaperDetailView
    # return dv.as_view()
    
class NewspaperListView(ListView):
    model = Newspaper
    
    
# class NewspaperDetailView(DetailView):
class NewspaperDetailView(ListView):
    model = Year