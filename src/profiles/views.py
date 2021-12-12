from django.shortcuts import redirect, render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

# Create your views here.
# TODO 
# Backend : Criar relação entre usuario e outros usuarios
# Fontend : Criar pagina post e editar post
# Frontend : Estilizar os accounts /base.html


def profile_Test_view(request):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:index'))
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/test_profile.html', {'profile':profile, 'testando': 'testaaaaaa'})

def MyProfileView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        if request.method == 'POST':
            return HttpResponseRedirect(reverse('profiles:index'))
        return render(request, 'profiles/my_profile.html')

def MyLikedRoute(request, name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
        
class MainPageView(TemplateView):
    template_name = 'profiles/main.html'
    
class RotaDeTesteDoHenrique(TemplateView):
    template_name = 'profiles\henriquo.html'
    
class RotaDeTesteDoZimmermmann(TemplateView):
    template_name = 'profiles\zimmermmann.html'
    
#class RotaDeTesteDoKrapp(View):
#    def get(self, *args, **kwargs):
#        return render(request, 'profiles/krapp.html')
    
def RotaDeTesteDoKrapp(request):
    return HttpResponseRedirect(reverse('profiles:index'))
    
class MyProfileData(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:index'))
        else:
            profile = Profile.objects.get(user=self.request.user)
            qs = profile.get_proposals_for_following()
            profiles_to_follow_list = []
            for user in qs:
                p = Profile.objects.get(user__username=user.username)
                profile_item = {
                    'username' : p.user.username,
                    'avatar' : p.avatar.url,
                    'bio' : p.bio
                }
                profiles_to_follow_list.append(profile_item)
            
            qsfeed = profile.get_my_and_following_posts()
            feedReturn = []
            for post in qsfeed:
                postdict = {}
                postdict['title'] = post.title
                postdict['author'] = post.author.user.username
                postdict['avatar'] = post.author.avatar.url
                feedReturn.append(postdict)
                
            return JsonResponse({'profiles_to_follow_list' : profiles_to_follow_list, 
                                 'username' : profile.user.username, 
                                 'avatar' : profile.avatar.url, 
                                 'followers' : profile.followers_count, 
                                 'following' : profile.following_count,
                                 'bio' : profile.bio,
                                 'feed': feedReturn})
        
            
        