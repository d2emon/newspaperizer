#coding: utf-8
from django.conf.urls import url
from article.views import ArticleDetailView


urlpatterns = [
    # url(r'^$', ArticleListView.as_view(), name='articles'),
    url(r'^(?P<np>[\w-]+)/(?P<year>\d+)/(?P<issue>\d+)/(?P<page>\d+)/$', ArticleDetailView.as_view(), name='article'),
]