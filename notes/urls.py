from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListView.as_view(), name="notes.list"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="notes.detail"),
    path("notes/popular/", views.PopularNotesListView.as_view(), name="notes.popular"),
]