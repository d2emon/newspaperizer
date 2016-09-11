#coding: utf-8
from django.conf.urls import url
from pdf.views import pdf_view


urlpatterns = [
    url(r'^(?P<np>[\w-]+)/(?P<year>\d+)/(?P<issue>\d+)/view.pdf$', pdf_view, name='pdf'),
]