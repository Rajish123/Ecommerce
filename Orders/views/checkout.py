from urllib import request
from Orders.models import Order
from django.views import View
from django.shortcuts import redirect, render
from Store.models import Product
from Accounts.models import Customer

# mport urllib.request
class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        # get customer id from session
        customer = request.session.get('customer')
        # cart = {'product':quantity}, get quantity from cart object
        cart = request.session.get('cart')
        print(cart.keys())
        # get all product ids
        products = Product.get_product_by_id(list(request.session.get('cart').keys()))
        print(products)
        # iterate all product to get price and to create order object
        for product in products:
            order = Order(
                # must pass customer object due to foreign key relation
                # create customer object
                customer = Customer(id = customer),
                product = product,
                price = product.price,
                address = address,
                phone = phone,
                quantity = cart.get(str(product.id))
            )
            order.placeOrder()
            # after order is placed, clear the cart
            request.session['cart'] = {}
        return redirect("store:cart")


