from django.urls import path

from .views import (
    profile_Test_view,
    RotaDeTesteDoKrapp,
    MyProfileData,
    MyProfileView,
    MainPageView,
    RotaDeTesteDoHenrique,
    RotaDeTesteDoZimmermmann
    
)

app_name = 'profiles'

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),                  
    path('test/', profile_Test_view, name='test_profile'),
    path('my/', MyProfileView.as_view(), name='my-profile-view'),
    path('my-profile-json/', MyProfileData.as_view(), name='my-profile-data'),
    path('henrique/', RotaDeTesteDoHenrique.as_view(), name='henrique'),
    path('zimmermmann/', RotaDeTesteDoZimmermmann.as_view(), name='zimmermmann'),
    path('krapp/', RotaDeTesteDoKrapp, name='krapp')
]