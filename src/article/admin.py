from django.contrib import admin
from article.models import ArticleCategory, Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Newspaper', {'fields': (('issue', 'page'), 'category')}),
        (None, {'fields': ('title', 'description')}),
    )
    

admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)