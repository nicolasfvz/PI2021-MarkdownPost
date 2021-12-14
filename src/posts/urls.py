from django.urls import path

from .views import (
    delete_post,
    edit_post,
    index,
    post,
    new_post,
    api
)

app_name = 'posts'

urlpatterns = [
    path('<str:profile>/<str:title>/', post, name='post'),
    path('new_post/', new_post, name='new_post'),
    path('<str:profile>/<str:title>/delete/', delete_post, name='delete'),
    path('', index, name='index'),
    path('api/', api, name='api'),
    path('<str:profile>/<str:title>/edit/', edit_post, name='edit')
]
