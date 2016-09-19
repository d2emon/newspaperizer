from django.contrib import admin
from world.models import World


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title', {'fields': (('title', 'slug'), )}),
        ('Image', {'fields': (('preview', 'image'), )}),
        ('Rating', {'fields': (('rating', ), )}),
    )
    list_display = ('title', 'preview', 'rating', )
    readonly_fields = ('preview', )
    prepopulated_fields = {'slug': ('title', )}
