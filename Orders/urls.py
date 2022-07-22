from django.urls import path
from .views import checkout, orders
from Store.middlewares.auth import auth_middleware

app_name = 'order'

urlpatterns = [
    path('total',checkout.total_payment),
    # path('checkout',auth_middleware(checkout.checkout_page),name = 'checkout_page'),
    
    path('checkout',auth_middleware(checkout.CheckOut.as_view()),name = 'checkout'),
    path('orders',auth_middleware(orders.OrderView.as_view()),name = 'orders'),
    # path('payment',checkout.payment, name = 'payment')
]

