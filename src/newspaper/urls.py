#coding: utf-8
from django.conf.urls import url
from newspaper.views import NewspaperListView, YearListView, IssueListView, ArticleListView


urlpatterns = [
    url(r'^np/$', NewspaperListView.as_view(), name='newspapers'),
    url(r'^np/(?P<np>[\w-]+)/$', YearListView.as_view(), name='year'),
    url(r'^np/(?P<np>[\w-]+)/(?P<year>\d+)/$', IssueListView.as_view(), name='issues'),
    url(r'^np/(?P<np>[\w-]+)/(?P<year>\d+)/(?P<issue>\d+)/$', ArticleListView.as_view(), name='issue'),
]