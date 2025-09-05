from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Note
from .forms import NoteForm

def add_like_view(request, pk):
    if request.method != "POST":
        raise Http404("Only POST method is allowed.")
    note = get_object_or_404(Note, pk=pk)
    note.likes += 1
    note.save()
    return HttpResponseRedirect(reverse('notes.detail', args=[pk, ]))

class NoteCreateView(CreateView):
    model = Note
    template_name = "notes/note_form.html"
    form_class = NoteForm
    success_url = "/smart/notes/"

class NoteUpdateView(UpdateView):
    model = Note
    template_name = "notes/note_form.html"
    form_class = NoteForm
    success_url = "/smart/notes/"

class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_delete.html"
    success_url = "/smart/notes/"

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