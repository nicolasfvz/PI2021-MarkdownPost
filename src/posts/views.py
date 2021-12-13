import json
import markdown
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from profiles.models import Profile

from .models import Post

# Create your views here.   profile = Profile.objects.get(user__username=profileGet)

def exact_profile(author):
    if (Profile.objects.filter(user__username=author).first() != None):
        return True
    else:
        return False

def exact_post(author, title):
    if exact_profile(author):
        profile = Profile.objects.get(user__username=author)
        if (Post.objects.filter(title=title, author=profile).first() != None):
            return True
        else:
            return False
    else:
        return False

def convert_markdown(value):
    a = markdown.markdown(value)
    return a

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

def edit_post(request, profile, title):
    if not request.user.is_authenticated:
            return None
    else:
        if exact_post(profile, title) == False:
            return HttpResponseRedirect(reverse('mainpage:index'))
        else:
            profile_que_ta_querendo = Profile.objects.filter(user__username=profile).first()
            if profile_que_ta_querendo.user != request.user:
                return HttpResponseRedirect(reverse('mainpage:index'))
            else:
                if request.method == 'POST':
                    new_title = request.POST["title"]
                    new_post = request.POST["creatingPost"]
                    print(title, post)
                    
                    if title == "" or post == "":
                        return HttpResponseRedirect(reverse('mainpage:index'))
                    else:
                        a = Post.objects.filter(title=title, author=profile_que_ta_querendo).update(title=new_title, body=new_post)
                        return HttpResponseRedirect(reverse('mainpage:index'))
                return render(request, 'posts/edit_post.html', {'perfil': profile, 'titulo':title})
    
    
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
        data['body'] = convert_markdown(post.body)
        print(convert_markdown(post.body))
        data['updated'] = post.updated
        data['created'] = post.created
        
    return JsonResponse({'post' : data})