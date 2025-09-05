from django.contrib import admin

from .models import Note

class NotesAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "likes")
    list_filter = ("created",)

admin.site.register(Note, NotesAdmin)