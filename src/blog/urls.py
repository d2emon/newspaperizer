# coding: utf-8
from django.conf.urls import url
from blog.views import NewsListView, NewsView


urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news'),
    url(r'^(?P<slug>[\w-]+)/$', NewsView.as_view(), name='news_article'),
]
