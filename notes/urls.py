from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListView.as_view(), name="all_notes"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    path("notes/popular/", views.PopularNotesListView.as_view(), name="popular_notes"),
]