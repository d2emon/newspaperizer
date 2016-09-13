from django.contrib import admin
from people.models import Person, Face, Hair, HairColor, Haircut, HairParting, EyeColor


class HairInline(admin.StackedInline):
    model = Hair


class FaceInline(admin.StackedInline):
    model = Face


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {'fields': (('first_name', 'nickname', 'last_name'), 'slug')}),
        ('Appearance', {'fields': ('body', 'arm', 'hand', 'leg', 'foot', )}),
        ('Description', {'fields': ('description', )}),
    )
    inlines = [FaceInline, HairInline]
    prepopulated_fields = {'slug': ('first_name', 'nickname', 'last_name')}


admin.site.register(HairColor)
admin.site.register(Haircut)
admin.site.register(HairParting)
admin.site.register(EyeColor)
