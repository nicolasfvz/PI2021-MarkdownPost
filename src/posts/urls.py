from django.urls import path

from .views import (
    index,
    post,
    api
)

app_name = 'posts'

urlpatterns = [
    path('<str:profile>/<str:title>/', post, name='post'),
    path('', index, name='index'),
    path('api/', api, name='api')
]