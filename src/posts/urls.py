from django.urls import path

from .views import (
    index,
    post,
    api
)

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('<str:profile>/<str:title>/', post, name='post'),
    path('api/', api, name='api')
]