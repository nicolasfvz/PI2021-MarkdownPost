import json
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from .models import Post

# Create your views here.

def index(request):
    return render(request, 'posts/main.html', {'hello' : 'hello world'})

def api(request):
    a = Post.objects.all()
    dic = {
        "title" : []
    }
    for i in a:
        dic["title"].append(i.title)

    json_object = json.dumps(dic)
    print(json_object)
    return HttpResponse(json_object)