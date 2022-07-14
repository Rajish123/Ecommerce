from django.urls import path
from . import views
from .views import signup,login,logout

app_name = "account"

urlpatterns = [
    path('signup',signup.SignUp.as_view(), name = 'signup'),
    path('log',login.Login.as_view(), name = 'login'),
    path('logout',logout.logout,name = 'logout'),
]
