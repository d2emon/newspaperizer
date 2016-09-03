#coding: utf-8
from django.conf.urls import url


from newspaper.views import NewspaperListView, NewspaperDetailView, YearListView, IssueListView, IssueDetailView
import newspaper.views


urlpatterns = [
    url(r'^$', NewspaperListView.as_view(), name='list'),
    url(r'^(?P<np>\d+)/$', YearListView.as_view(), name='year'),
    url(r'^(?P<np>\d+)/(?P<year>\d+)/$', IssueListView.as_view(), name='issues'),
    url(r'^(?P<np>\d+)/(?P<year>\d+)/(?P<issue>\d+)/$', IssueDetailView.as_view(), name='issue'),
    url(r'^hello/$', newspaper.views.index, name='hello'),
    url(r'^n/(?P<pk>\d+)/$', newspaper.views.years),
    url(r'^years/(?P<pk>\d+)/$', NewspaperDetailView.as_view(), name='years'),
    # url(r'^(?P<pk>\d+)/$', NewspaperDetailView.as_view()),
]