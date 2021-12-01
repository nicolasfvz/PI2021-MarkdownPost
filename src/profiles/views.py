from django.shortcuts import redirect, render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

# Create your views here.
# TODO Backend : Criar relação entre usuario e outros usuarios
# Backend : Annonymous error MyProfileData
# Frontend : Criar pagina de perfil aceitavel
# Frontend : Estilizar os accounts /base.html

def profile_Test_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/test_profile.html', {'profile':profile, 'testando': 'testaaaaaa'})

def MyProfileView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        return render(request, 'profiles/my_profile.html')

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
            return None
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
            return JsonResponse({'profiles_to_follow_list' : profiles_to_follow_list, 'username' : profile.user.username, 'avatar' : profile.avatar.url, 'followers' : profile.followers_count, 'following' : profile.following_count})
        
            
        