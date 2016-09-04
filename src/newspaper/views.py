from django.views.generic import ListView
from newspaper.models import Newspaper, Year, Issue
from article.models import Article


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
    
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": Newspaper.objects.get(pk=self.kwargs.get('np')),                        
            "year": Year.objects.get(year=self.kwargs.get('year')),                        
        })
        return context

    
class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        newspaper_id = self.kwargs.get('np')
        year_id = self.kwargs.get('year')
        issue_id = self.kwargs.get('issue')
        
        np = Newspaper.objects.get(pk=newspaper_id)
        year = Year.objects.get(year=year_id)
        issue = Issue.objects.get(newspaper=np, year=year, issue=issue_id)
        
        return self.model.objects.filter(issue=issue).distinct()
    
    def get_context_data(self, **kwargs):
        newspaper_id = self.kwargs.get('np')
        year_id = self.kwargs.get('year')
        issue_id = self.kwargs.get('issue')
        
        np = Newspaper.objects.get(pk=newspaper_id)
        year = Year.objects.get(year=year_id)

        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": np,                        
            "year": year,                        
            "issue": Issue.objects.get(newspaper=np, year=year, issue=issue_id),                        
        })
        return context