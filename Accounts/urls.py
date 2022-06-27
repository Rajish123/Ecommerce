from django.urls import path
from . import views
from .views import SignUp,Login

app_name = "account"

urlpatterns = [
    path('signup/',SignUp.as_view(), name = 'signup'),
    path('login/',Login.as_view(), name = 'login'),
]
