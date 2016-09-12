from django.contrib import admin
from people.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {'fields': (('first_name', 'nickname', 'last_name'), 'slug')}),
        ('Description', {'fields': ('description', )}),
    )
    # inlines = [IssueInline]
    prepopulated_fields = {'slug': ('first_name', 'nickname', 'last_name')}
