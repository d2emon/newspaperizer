from django.views.generic import ListView
from newspaper.models import Newspaper, Year, Issue
from article.models import Article
from template.models import ArticleTemplate
from django.shortcuts import redirect


def get_newspaper(slug):
    return Newspaper.objects.get(slug=slug)


def get_year(year):
    return Year.objects.get(year=year)


def get_issue(np, year, issue):
    return Issue.objects.get(newspaper=np, year=year, issue=issue)


def generate(request, **kwargs):
    newspaper_id = kwargs.get('np')
    year_id = kwargs.get('year')
    issue_id = kwargs.get('issue')
    np = get_newspaper(newspaper_id)
    year = get_year(year_id)
    issue = get_issue(np, year, issue_id)

    templates = ArticleTemplate.objects.filter(newspaper=np).all()
    print(kwargs)
    for template in templates:
        print()
        print(template)
        print(
            template.category,
            template.article_type,
            template.page,
        )
        print()
        page = Article(
            issue=issue,
            category=template.category,
            article_type=template.article_type,
            page=template.page,
        )
        print(page)
        print()
        print("Title: ", page.title)
        print("Category: ", page.category)
        print("Article Type: ", page.article_type)
        # page.linked,
        print(
            page.description,
        )
    return redirect(issue.url())


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
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())

        context = ListView.get_context_data(self, **kwargs)
        context.update({
            "np": np,
            "year": year,
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

    def dispatch(self, request, *args, **kwargs):
        np = get_newspaper(self.newspaper_id())
        year = get_year(self.year_id())
        issue = get_issue(np, year, self.issue_id())

        try:
            return redirect(issue.title_page().url())
        except Article.DoesNotExist:
            return super(ArticleListView, self).dispatch(request, *args, **kwargs)
