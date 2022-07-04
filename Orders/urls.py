from django.urls import path
from .views import checkout

app_name = 'order'

urlpatterns = [
    path('checkout',checkout.CheckOut.as_view(),name = 'checkout')
]

