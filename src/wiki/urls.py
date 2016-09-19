# coding: utf-8
from django.conf.urls import url
from django.views.generic.base import RedirectView
from wiki.views import PageView


urlpatterns = [
    url(r'^(?P<path>.*)/$', PageView.as_view(), name='wiki'),
    url(r'^(?P<path>.*)^/$', RedirectView.as_view(pattern_name='wiki')),
]
