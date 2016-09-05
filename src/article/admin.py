from django.contrib import admin
from article.models import ArticleCategory, ArticleType, Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Newspaper', {'fields': (('issue', 'page'), 'category')}),
        ('Type', {'fields': ('article_type', )}),
        ('Content', {'fields': ('title', 'description')}),
        ('Links', {'fields': ('linked', )})
    )
    list_filter = ('issue__year', 'issue', 'page', )
    # date_hierarchy = 'issue_date' 
    # raw_id_fields = ('issue', )
    # list_display = ('title', 'issue', 'page')
    

admin.site.register(ArticleCategory)
admin.site.register(ArticleType)
admin.site.register(Article, ArticleAdmin)