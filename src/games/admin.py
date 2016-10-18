from django.contrib import admin
from games.models import VideoGameGenre, OutdoorGame, BoardGame, RoleplayGame, GameBook, VideoGame

# @admin.register(VideoGameGenre)
# class VideoGameGenreAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Title', {'fields': (('title', 'slug'), )}),
    #     ('Image', {'fields': (('preview', 'image'), )}),
    #     ('Rating', {'fields': (('rating', ), )}),
    # )
    # list_display = ('title', 'preview', 'rating', )
    # readonly_fields = ('preview', )
    # prepopulated_fields = {'slug': ('title', )}

admin.site.register(OutdoorGame)
admin.site.register(BoardGame)
admin.site.register(RoleplayGame)
admin.site.register(GameBook)

@admin.register(VideoGameGenre)
@admin.register(VideoGame)
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
