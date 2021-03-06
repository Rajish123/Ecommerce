from itertools import product
from Store.models import Product
from django.views import View
from django.shortcuts import render

class Cart(View):
    def get(self,request):
        # retrieve list of products or product id you added in cart from cart session
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request,'cart.html',{'products':products})