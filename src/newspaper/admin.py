from django.contrib import admin
from newspaper.models import Newspaper, Year, Issue


class IssueInline(admin.TabularInline):
    model = Issue
    extra = 3


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    inlines = [IssueInline]
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Year)
# admin.site.register(Newspaper, NewspaperAdmin)
