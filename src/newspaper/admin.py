from django.contrib import admin
from newspaper.models import Newspaper, Year, Issue


class IssueInline(admin.TabularInline):
    model = Issue
    extra = 3
    

class NewspaperAdmin(admin.ModelAdmin):
    inlines = [IssueInline]


admin.site.register(Issue)
admin.site.register(Year)
admin.site.register(Newspaper, NewspaperAdmin)