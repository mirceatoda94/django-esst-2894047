from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = "notes/notes_list.html"
    context_object_name = "notes"
    ordering = ['created']

class PopularNotesListView(ListView):
    model = Note
    template_name = "notes/popular_notes_list.html"
    context_object_name = "popular_notes"

    def get_queryset(self):
        return Note.objects.filter(likes__gte=3).order_by('-likes')

class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"