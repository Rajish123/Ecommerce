from django.urls import path
from .views import index,cart

app_name = 'store'

urlpatterns = [
    path('',index.IndexView.as_view(), name = 'index'),
    path('cart',cart.Cart.as_view(),name = 'cart')
]
