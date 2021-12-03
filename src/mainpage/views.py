
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

# Create your views here.

class Mainpage(TemplateView):
    template_name = 'mainpage/main.html'