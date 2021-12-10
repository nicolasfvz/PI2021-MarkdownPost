from django.urls import path

from .views import (
    index,
    post,
    new_post,
    api
)

app_name = 'posts'

urlpatterns = [
    path('<str:profile>/<str:title>/', post, name='post'),
    path('new_post/', new_post, name='new_post'),
    path('', index, name='index'),
    path('api/', api, name='api')
]
