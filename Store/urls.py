from django.urls import path
from .views import index,cart,home,about
from Store.middlewares.auth import auth_middleware

app_name = 'store'

urlpatterns = [
    # homepage
    path('home',home.HomeView.as_view(), name = 'home'),
    path('about',about.AboutView.as_view(), name = 'about'),

    # allproduct
    # path('product',index.IndexView.as_view(),name = 'product'),
    path('',index.IndexView.as_view(), name = 'index'),
    path('cart',auth_middleware(cart.Cart.as_view()),name = 'cart'),
]
