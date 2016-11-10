from django.contrib import admin
from speccy.models import BookGames


@admin.register(BookGames)
class SluggedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
