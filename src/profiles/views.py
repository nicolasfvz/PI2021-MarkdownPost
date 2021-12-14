from django.shortcuts import redirect, render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

# Create your views here.
# TODO 
# Backend : Fazer o botão de exluir post
# Backend : Fazer o botão de follow do modal funcionar
# Backend : Fazer o botão de random page funcionar
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
            perfil = Profile.objects.get(user=request.user)
            perfil.bio = request.POST["bio"] 
            perfil.avatar = request.FILES["avatar"]
            perfil.save()       
            return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        return render(request, 'profiles/my_profile.html')

def ProfileView(request, profile_name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        if request.method == "POST":
            perfil = Profile.objects.get(user=request.user)
            perfil_do_link = Profile.objects.get(user__username=profile_name)
        
            if perfil_do_link.user in perfil.get_following():
                perfil.following.remove(perfil_do_link.user)
                return HttpResponseRedirect(reverse('profiles:my-profile-view'))
            else:
                perfil.following.add(perfil_do_link.user)
                return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        else:
                
            frase = "Follow"
            perfil = Profile.objects.get(user=request.user)
            perfil_do_link = Profile.objects.get(user__username=profile_name).user

            if perfil_do_link in perfil.get_following():
                frase = "Unfollow"
            return render(request, 'profiles/profile.html', {"nome" : profile_name, "seguir" : frase})
    
def ProfileJson(request, profile_name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        profile = Profile.objects.get(user__username=profile_name)
        feed = [i.title for i in profile.get_my_post()]
        return JsonResponse({'name' : f"{profile.user.username}",
                            'avatar' : f"{profile.avatar.url}",
                            'bio' : f"{profile.bio}",
                            'feed' : feed,
                            'followers' : profile.followers_count, 
                            'following' : profile.following_count})
        
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
        
            
        