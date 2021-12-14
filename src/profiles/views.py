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
        
            

# def criarNFTde200Milhoes():
#     # all image credits goes to https://picrew.me/image_maker/1360413, I stole it :+1:

#     # Importa LIBS
#     import os, random
#     import hashlib

#     curr_dir = str(os.path.dirname(os.path.realpath(__file__)))

#     # Importa a bibliotecx de edição de imagens
#     try:
#         from PIL import Image
#     except ImportError:
#         import Image

#     # Gera o/a id inicial do/a ape/a gerado/a
#     monkeName = ''

#     # Gera as camadx
#     bgid      = str(random.choice(os.listdir(".\\bg")))
#     skinid    = str(random.choice(os.listdir(".\\skin")))
#     bocaid    = str(random.choice(os.listdir(".\\boca")))
#     camisaid  = str(random.choice(os.listdir(".\\camisa")))
#     olesosid  = str(random.choice(os.listdir(".\\oleos")))
#     oculosid  = str(random.choice(os.listdir(".\\oculo")))
#     cha_peuid = str(random.choice(os.listdir(".\\cha peu")))

#     # Seta
#     bgDir      = curr_dir +  '\\bg\\'      + bgid
#     skinDir    = curr_dir +  '\\skin\\'    + skinid
#     bocaDir    = curr_dir +  '\\boca\\'    + bocaid
#     camisaDir  = curr_dir +  '\\camisa\\'  + camisaid
#     olesosDir  = curr_dir +  '\\oleos\\'   + olesosid
#     oculosDir  = curr_dir +  '\\oculo\\'   + oculosid
#     cha_peuDir = curr_dir +  '\\cha peu\\' + cha_peuid


#     # gera um id com base nas camadas escolhidas
#     apename = [

#          bgid.replace('.png', ''),
#        skinid.replace('.png', ''),
#        bocaid.replace('.png', ''),
#      camisaid.replace('.png', ''),
#      olesosid.replace('.png', ''),
#      oculosid.replace('.png', ''),
#     cha_peuid.replace('.png', '')

#     ]


#     for i in apename:
#         monkeName += i
#         monkeName += 'Penis'

#     #define o nome
#     monkeName = hashlib.md5(monkeName.encode('utf-8')).hexdigest()
    
#     print(monkeName)    

#     # Abre eles/elas para trabalhar com eles/elas
#     L1 = Image.open(bgDir)
#     L2 = Image.open(skinDir)
#     L3 = Image.open(bocaDir)
#     L4 = Image.open(camisaDir)
#     L5 = Image.open(olesosDir)
#     L6 = Image.open(oculosDir)
#     L7 = Image.open(cha_peuDir)

#     # Converte-(o)as para RGBA
#     F1 = L1.convert("RGBA")
#     F2 = L2.convert("RGBA")
#     F3 = L3.convert("RGBA")
#     F4 = L4.convert("RGBA")
#     F5 = L5.convert("RGBA")
#     F6 = L6.convert("RGBA")
#     F7 = L7.convert("RGBA")

#     # Estaca-(o)as
#     IMG = Image.alpha_composite(F1 , F2)
#     IMG = Image.alpha_composite(IMG, F3)
#     IMG = Image.alpha_composite(IMG, F4)
#     IMG = Image.alpha_composite(IMG, F5)
#     IMG = Image.alpha_composite(IMG, F6)
#     IMG = Image.alpha_composite(IMG, F7)


#     # Seta o caminhx para 
#     apes = curr_dir + '\\apes'

#     # totalFiles = 0

#     # # Verifica quantxs arquivxs tem nas pastxs
#     # for base, dirs, files in os.walk(apes):
#     #     for Files in files:
#     #         totalFiles += 1


#     # Gera o diretorixs para salvar
#     filename = f"\\{monkeName}.png"
#     dirToSave = apes + filename

#     # print(dirToSave)

#     # Checx se o/a arquivo existe
#     if os.path.isfile(dirToSave):
#        print("\nErro, esse arquivo ja existe,", dirToSave, '\nresolve isso ae sla, fiquei com preguiça de pensar em uma solução\n')
#     else:
#         IMG.save(dirToSave,"PNG")


# criarNFTde200Milhoes()



