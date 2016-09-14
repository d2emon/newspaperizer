# coding: utf-8
from django.conf.urls import url
from world.views import WorldListView, WikiListView, WorldDetailView, random_world


urlpatterns = [
    url(r'^$', WorldListView.as_view(), name='worlds'),
    url(r'^__page.opt$', WikiListView.as_view(), name='worlds_wiki'),
    url(r'^random/$', random_world, name='random_world'),
    url(r'^(?P<slug>[\w-]+)/view/$', WorldDetailView.as_view(), name='world'),
]
