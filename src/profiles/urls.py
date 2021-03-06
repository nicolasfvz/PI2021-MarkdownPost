from django.urls import path

from .views import (
    ProfileJson,
    ProfileView,
    profile_Test_view,
    RotaDeTesteDoKrapp,
    MyProfileView,
    MyLikedRoute,
    MainPageView,
    MyProfileData,
    RotaDeTesteDoHenrique,
    RotaDeTesteDoZimmermmann
    
)

app_name = 'profiles'

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),                  
    path('test/', profile_Test_view, name='test_profile'),
    path('profile-json/<str:profile_name>', ProfileJson, name='profile-json'),
    path('my/', MyProfileView, name='my-profile-view'),
    path('my-profile-json/', MyProfileData.as_view(), name='my-profile-data'),
    path('like/<str:name>', MyLikedRoute, name='like'),
    path('<str:profile_name>/', ProfileView, name='profile'),
    #  Test routes
    path('henrique/', RotaDeTesteDoHenrique.as_view(), name='henrique'),
    path('zimmermmann/', RotaDeTesteDoZimmermmann.as_view(), name='zimmermmann'),
    path('krapp/', RotaDeTesteDoKrapp, name='krapp')
]