from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import randint

from .models import Posts
from .until import exact_post
# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html", {
        "post_info" : Posts.objects.all()
    })
    #return render(request, "flights/index.html", {
    #    "flights" : Flight.objects.all()
    #})

def title(request, entry_title):
    
    if(exact_post(entry_title) == False):
        return render(request, "encyclopedia/not_found.html")
    post = Posts.objects.get(title=entry_title)
    return render(request, "encyclopedia/post.html", {
        "title": post.title,
        "post": post.post
    })

def random(request):
    aleatorio = len(Posts.objects.all())
    post = Posts.objects.get(id=randint(1, aleatorio)+1)
    return HttpResponseRedirect(reverse("title", args=(post.title,)))

def new_post(request):
    if request.method == 'POST':
        title = request.POST["title"]
        post = request.POST["post_info"]
        print(f"{title}, {post}")
        if title == "" or post == "":
            return HttpResponseRedirect(reverse("new_post"))
        else:
            new_post = Posts(title=title, post=post)
            new_post.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/new_post.html")

def edit(request, entry_title):
    if(exact_post(entry_title) == False):
        return render(request, "encyclopedia/not_found.html")
    else:
        if request.method == 'POST':
            title = request.POST["title"]
            post = request.POST["post_info"]
            if title == "" or post == "":
                return HttpResponseRedirect(reverse("index"))
            else:
                a = Posts.objects.filter(title=entry_title).update(title=title, post=post)
                #a.save()
                return HttpResponseRedirect(reverse("index"))
        post = Posts.objects.get(title=entry_title)
        #if post == None:
        #    return HttpResponseRedirect(reverse("index"))
        return render(request, "encyclopedia/edit_post.html", {
            "title": entry_title,
            "post": post.post
    })

def search(request):
    value = request.GET.get('q', '')
    if (exact_post(value)):
        return HttpResponseRedirect(reverse("title", args=(value,)))
