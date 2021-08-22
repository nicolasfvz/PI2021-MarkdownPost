from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random", views.random, name="random"),
    path("wiki/new_post", views.new_post, name="new_post"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<str:entry_title>", views.title, name="title"),
    path("wiki/<str:entry_title>/edit", views.edit, name="edit")
]