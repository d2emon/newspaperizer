from django.http import HttpResponse
from django.views.generic import ListView # , DetailView
from newspaper.models import Newspaper, Year


def index(request):
    return HttpResponse("Hello world!")

def years(request, pk):
    np = Newspaper.objects.get(pk=pk)
    # issues = np.get_issues()
    print(np)
    print(np.issue_set.all())
    return HttpResponse(np)
    # dv = NewspaperDetailView
    # return dv.as_view()
    
class NewspaperListView(ListView):
    model = Newspaper
    
    
# class NewspaperDetailView(DetailView):
class NewspaperDetailView(ListView):
    model = Newspaper.objects.get(pk=1).issue_set.all()