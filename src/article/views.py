from django.views.generic import DetailView
from newspaper.models import Newspaper, Year, Issue
from article.models import Article

class ArticleDetailView(DetailView):
    model = Article
    
    def get_object(self, queryset=None):
        newspaper_id = self.kwargs.get('np')
        year_id = self.kwargs.get('year')
        issue_id = self.kwargs.get('issue')
        page_id = self.kwargs.get('page')
                
        np = Newspaper.objects.get(pk=newspaper_id)
        year = Year.objects.get(year=year_id)
        issue = Issue.objects.get(newspaper=np, year=year, issue=issue_id)
        
        return self.model.objects.get(issue=issue, page=page_id)