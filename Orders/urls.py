from django.urls import path
from .views import checkout, orders

app_name = 'order'

urlpatterns = [
    path('checkout',checkout.CheckOut.as_view(),name = 'checkout'),
    path('orders',orders.OrderView.as_view(),name = 'orders')
]

