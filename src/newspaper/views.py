from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from newspaper.models import Newspaper, Year, Issue


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
    
    
class YearListView(ListView):
    model = Year   
    
    def get_queryset(self):
        newspaper_id = self.kwargs.get('np')
        np = Newspaper.objects.get(pk=newspaper_id)
        return self.model.objects.filter(issue__newspaper=np).distinct()
    
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": Newspaper.objects.get(pk=self.kwargs.get('np')),                        
        })
        return context

    
class IssueListView(ListView):
    model = Issue

    def get_queryset(self):
        newspaper_id = self.kwargs.get('np')
        year_id = self.kwargs.get('year')
        np = Newspaper.objects.get(pk=newspaper_id)
        year = Year.objects.get(year=year_id)
        return self.model.objects.filter(newspaper=np, year=year).distinct()
    
class IssueDetailView(DetailView):
    model = Issue
    
    def get_object(self):
        newspaper_id = self.kwargs.get('np')
        year_id = self.kwargs.get('year')
        issue_id = self.kwargs.get('issue')
        np = Newspaper.objects.get(pk=newspaper_id)
        year = Year.objects.get(year=year_id)
        return self.model.objects.get(newspaper=np, year=year, issue=issue_id)
    
    
# class NewspaperDetailView(DetailView):
class NewspaperDetailView(ListView):
    model = Issue
    
    # def get_queryset(self):
        # return self.model.objects.filter(newspaper=1)