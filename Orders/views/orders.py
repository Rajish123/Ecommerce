from urllib import request
from Orders.models import Order
from django.views import View
from django.shortcuts import render
# from Store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

class OrderView(View):
    # alternative ways to use middleware is in urls.py
    # @method_decorator(auth_middleware)
    def get(self, request):
        # return customer id
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request,'orders.html',{'orders':orders})