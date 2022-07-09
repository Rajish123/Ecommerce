from django.urls import path
from .views import index,cart,home,about

app_name = 'store'

urlpatterns = [
    # homepage
    path('',home.HomeView.as_view(), name = 'home'),
    path('about',about.AboutView.as_view(), name = 'about'),

    # allproduct
    # path('product',index.IndexView.as_view(),name = 'product'),
    # path('',index.IndexView.as_view(), name = 'index'),
    path('cart',cart.Cart.as_view(),name = 'cart'),
]
