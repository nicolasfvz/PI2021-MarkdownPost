import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import randint

from .models import Posts
from .until import exact_post
# Create your views here.

def index(request):
    """This is the function that run when the main page is requested

    Args:
        request ([GET]):        The request that the web browser gives the server

    Returns:
        [Class: HttpResponse]:  The render function return a object HttpResponse, that gives you the main web page
    """
    return render(request, "encyclopedia/index.html", {
        "post_info" : Posts.objects.all()
    })
    #return render(request, "flights/index.html", {
    #    "flights" : Flight.objects.all()
    #})

def title(request, entry_title):
    """This is the function that run when the page of a certain post is requested

    Args:
        request ([GET]):        The request that the web browser gives the server
        entry_title ([str]):    The title of the post that you want to see

    Returns:
        [Class: HttpResponse]: Gives you the web page that you want
    """
    if(exact_post(entry_title) == False):
        return render(request, "encyclopedia/not_found.html")
    post = Posts.objects.get(title=entry_title)
    return render(request, "encyclopedia/post.html", {
        "title": post.title,
        "post": post.post
    })

def random(request):
    """This is the function that run when the page of a random post is requested

    Args:
        request ([GET]):        The request that the web browser gives the server

    Returns:
        [Class: HttpResponse]:  Gives you the web page that you want
    """
    aleatorio = len(Posts.objects.all())
    post = Posts.objects.get(id=randint(1, aleatorio))
    return HttpResponseRedirect(reverse("title", args=(post.title,)))

def new_post(request):
    """This is the function that run when the user wants to create a new post

    Args:
        request ([GET/POST]):   The request that the web browser gives the server
                                If the request is a GET, it will render the page to create a new post.
                                If the request is a POST, it means that the user already made the post and its requesting to be added.

    Returns:
        [Class: HttpResponse]:  If the request is a GET, it will return the page to create a new post
                                If the request is a POTS, and the post recived it's valid, it will return to the main page
                                Otherwise it will return the 'new_post' page
    """
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
    """This is the function that run when the user wants to edit a post

    Args:
        request ([GET/POST]):   The request that the web browser gives the server
                                If the request is a GET, it will render the page to edit a post.
                                If the request is a POST, it means that the user already made the editions of the post and its requesting to be edited.

        entry_title ([str]):    The title of the post that you want to edit

    Returns:
        [Class: HttpResponse]:  If the request is a GET, it will return the page to edit a post
                                If the request is a POST, and the post recived it's valid, it will return to the main page
                                Otherwise it will return the main page
    """
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
    """This is the function that run when the user wants to search a post

    Args:
        request ([GET]): The request that the web browser gives the server

    Returns:
        [Class: HttpResponse]:  The render function return a object HttpResponse, that gives you the web page that you want.
    """
    value = request.GET.get('q', '')
    if (exact_post(value)):
        return HttpResponseRedirect(reverse("title", args=(value,)))

def api(request):
    a = Posts.objects.all()
    dic = {
        "title" : []
    }
    for i in a:
        dic["title"].append(i.title)

    json_object = json.dumps(dic)
    print(json_object)
    return HttpResponse(json_object)