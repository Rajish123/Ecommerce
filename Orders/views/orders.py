from urllib import request
from Orders.models import Order
from django.views import View
from django.shortcuts import redirect, render

# mport urllib.request
class OrderView(View):
    def get(self, request):
        # return customer id
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request,'orders.html',{'orders':orders})