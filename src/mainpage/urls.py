from django.urls import path

from .views import (
    Mainpage
)

app_name = 'mainpage'

urlpatterns = [
    path('', Mainpage.as_view(), name='index')
]