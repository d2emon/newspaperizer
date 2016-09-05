from django.views.generic import DetailView
from newspaper.models import Newspaper, Year, Issue
from article.models import Article
from newspaper.views import get_newspaper, get_year, get_issue

class ArticleDetailView(DetailView):
    model = Article

    def newspaper_id(self):
        return self.kwargs.get('np')

    def year_id(self):
        return self.kwargs.get('year')

    def issue_id(self):
        return self.kwargs.get('issue')
    
    def get_object(self, queryset=None):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        issue = get_issue(np, year, self.issue_id())

        page_id = self.kwargs.get('page')
        
        return self.model.objects.get(issue=issue, page=page_id)
    
    def get_context_data(self, **kwargs):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        issue = get_issue(np, year, self.issue_id())
        
        context = DetailView.get_context_data(self, **kwargs)
        context.update({
            "np": np,                        
            "year": year,                        
            "issue": issue,                        
        })
        return context    