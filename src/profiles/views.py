from django.shortcuts import render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect

# Create your views here.
""" 
"""
def profile_Test_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/test_profile.html', {'profile':profile})

class MainPageView(TemplateView):
    template_name = 'profiles/main.html'

class MyProfileView(TemplateView):
    template_name = 'profiles/my_profile.html'
    
class RotaDeTesteDoHenrique(TemplateView):
    template_name = 'profiles\henriquo.html'
    
class RotaDeTesteDoZimmermmann(TemplateView):
    template_name = 'profiles\zimmermmann.html'
    
#class RotaDeTesteDoKrapp(View):
#    def get(self, *args, **kwargs):
#        return render(request, 'profiles/krapp.html')
    
def RotaDeTesteDoKrapp(request):
    if request.method == 'POST':
        print("waaario")
        return HttpResponseRedirect('zimmermmann')
    return render(request, 'profiles/krapp.html')
    
class MyProfileData(View):
    def get(self, *args, **kwargs):
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