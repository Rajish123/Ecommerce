from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('signup/',views.SignUp, name = 'signup'),
    path('login/',views.Login, name = 'login'),
]
