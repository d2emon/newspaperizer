from django.contrib import admin
from newspaper.models import Newspaper, Year, Issue

admin.site.register(Newspaper)
admin.site.register(Year)
admin.site.register(Issue)