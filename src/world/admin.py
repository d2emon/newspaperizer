from django.contrib import admin
from world.models import World


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title', {'fields': (('title', 'slug'), )}),
        ('Image', {'fields': (('preview', 'image'), )}),
        ('Description', {'fields': ('description', )}),
    )
    readonly_fields = ('preview', )
    prepopulated_fields = {'slug': ('title', )}
