from django.urls import path

from .views import (
    profile_Test_view,
    MyProfileData,
    MyProfileView
)

app_name = 'profiles'

urlpatterns = [
    path('test/', profile_Test_view, name='test_profile'),
    path('my/', MyProfileView.as_view(), name='my-profile-view'),
    path('my-profile-json/', MyProfileData.as_view(), name='my-profile-data')
]