from django.contrib import admin
from book.models import BookGenre, ScienceBook


@admin.register(BookGenre)
@admin.register(ScienceBook)
class SluggedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

# admin.site.register(BookGenre)
# admin.site.register(Book)
