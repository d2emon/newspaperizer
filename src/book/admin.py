from django.contrib import admin
from book.models import BookGenre, Book


@admin.register(BookGenre)
@admin.register(Book)
class SluggedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

# admin.site.register(BookGenre)
# admin.site.register(Book)
