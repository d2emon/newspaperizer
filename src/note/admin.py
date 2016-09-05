from django.contrib import admin
from note.models import NoteType, Note


@admin.register(Note)    
class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
        

admin.site.register(NoteType)