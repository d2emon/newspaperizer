#coding: utf-8
from django.conf.urls import url


from newspaper.views import NewspaperListView, NewspaperDetailView


urlpatterns = [
    url(r'^$', NewspaperListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', NewspaperDetailView.as_view()),
]