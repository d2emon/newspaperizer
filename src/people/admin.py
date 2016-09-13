from django.contrib import admin
from people.models import Person, Male, Female, Face, Hair, Breast, Cloth, BreastSize, HairColor, Haircut, HairParting, EyeColor


class HairInline(admin.TabularInline):
    model = Hair


class FaceInline(admin.StackedInline):
    model = Face


class BreastInline(admin.TabularInline):
    model = Breast


class ClothInline(admin.TabularInline):
    model = Cloth


@admin.register(Person)
@admin.register(Male)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {'fields': (('first_name', 'nickname', 'last_name'), 'slug')}),
        ('Appearance', {'fields': ('body', 'arm', 'hand', 'leg', 'foot', )}),
        ('Description', {'fields': ('description', )}),
    )
    inlines = [HairInline, FaceInline, ClothInline]
    prepopulated_fields = {'slug': ('first_name', 'nickname', 'last_name')}


@admin.register(Female)
class FemaleAdmin(PersonAdmin):
    inlines = [HairInline, FaceInline, BreastInline, ClothInline]


admin.site.register(BreastSize)

admin.site.register(HairColor)
admin.site.register(Haircut)
admin.site.register(HairParting)
admin.site.register(EyeColor)
