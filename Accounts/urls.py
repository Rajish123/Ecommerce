from django.urls import path
from . import views
from .views import signup,login,logout,profile,update_profile,change_password

app_name = "account"

urlpatterns = [
    path('signup/',signup.SignUp.as_view(), name = 'signup'),
    path('log',login.Login.as_view(), name = 'login'),
    path('logout',logout.logout,name = 'logout'),
    path('profile',profile.Profile.as_view(),name='profile'),
    path('update_profile',update_profile.UpdateProfile.as_view(),name='update_profile'),
    path('change_password',change_password.ChangePassword.as_view(),name = 'change_password')
]
