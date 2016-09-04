from django.views.generic import ListView
from newspaper.models import Newspaper, Year, Issue
from article.models import Article


def get_newspaper(slug):
    return Newspaper.objects.get(slug=slug)


def get_year(year):
    return Year.objects.get(year=year)


def get_issue(np, year, issue):
    return Issue.objects.get(newspaper=np, year=year, issue=issue)


class NewspaperListView(ListView):
    model = Newspaper
    
    
class YearListView(ListView):
    model = Year   
    
    def newspaper_id(self):
        return self.kwargs.get('np')

    def get_queryset(self):
        np = get_newspaper(self.newspaper_id())
        
        return self.model.objects.filter(issue__newspaper=np).distinct()
    
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": get_newspaper(self.kwargs.get('np')),                        
        })
        return context

    
class IssueListView(ListView):
    model = Issue

    def newspaper_id(self):
        return self.kwargs.get('np')

    def year_id(self):
        return self.kwargs.get('year')

    def get_queryset(self):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        
        return self.model.objects.filter(newspaper=np, year=year).distinct()
    
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": get_newspaper(self.newspaper_id()),                        
            "year": get_year(self.year_id()),                        
        })
        return context

    
class ArticleListView(ListView):
    model = Article

    def newspaper_id(self):
        return self.kwargs.get('np')

    def year_id(self):
        return self.kwargs.get('year')

    def issue_id(self):
        return self.kwargs.get('issue')

    def get_queryset(self):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        issue = get_issue(np, year, self.issue_id())
        
        return self.model.objects.filter(issue=issue).distinct()
    
    def get_context_data(self, **kwargs):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        issue = get_issue(np, year, self.issue_id())
        
        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": np,                        
            "year": year,                        
            "issue": issue,                        
        })
        return context