#coding: utf-8
from django.conf.urls import url


from newspaper.views import NewspaperListView, NewspaperDetailView
import newspaper.views


urlpatterns = [
    url(r'^$', NewspaperListView.as_view(), name='list'),
    url(r'^hello$', newspaper.views.index, name='hello'),
    url(r'^(?P<pk>\d+)/$', newspaper.views.years),
    # url(r'^(?P<pk>\d+)/$', NewspaperDetailView.as_view()),
]