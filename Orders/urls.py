from django.urls import path
from .views import checkout, orders
from Store.middlewares.auth import auth_middleware

app_name = 'order'

urlpatterns = [
    path('checkout',checkout.CheckOut.as_view(),name = 'checkout'),
    path('orders',auth_middleware(orders.OrderView.as_view()),name = 'orders')
]

