import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from profiles.models import Profile

from .models import Post

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
            return None
    else:
        return render(request, 'posts/main.html', {'hello' : 'hello world'})

def post(request, profile, title):
    if not request.user.is_authenticated:
            return None
    else:
        return render(request, 'posts/post.html', {'perfil': profile, 'titulo':title})

def new_post(request):
    if not request.user.is_authenticated:
        return None
    else:
        if request.method == 'POST':
                
            title = request.POST["title"]
            post = request.POST["creatingPost"]
            
            if title == "" or post == "":
                return HttpResponseRedirect(reverse('mainpage:index'))
            
            profile = Profile.objects.get(user__username=request.user)
            new_post = Post(title=title, body=post, author=profile)
            new_post.save()
            
            return HttpResponseRedirect(reverse('mainpage:index'))
        return render(request, 'posts/new_post.html')

def api(request):
    profileGet = request.GET.get('profile', '')
    postGet = request.GET.get('post', '')
    
    profile = Profile.objects.get(user__username=profileGet)
    
    qs = Post.objects.filter(author=profile.pk).filter(title=postGet)
    data = {}
    for post in qs:
        data['title'] = post.title
        data['body'] = post.body
        data['updated'] = post.updated
        data['created'] = post.created
        
    return JsonResponse({'post' : data})