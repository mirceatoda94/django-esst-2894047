from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("authorized/", views.authorized_view, name="authorized"),
]