from importlib import resources
from itertools import product
from urllib import request
from Orders.models import Order
from django.views import View
from django.shortcuts import redirect, render, HttpResponse
from Store.models import Product
from Accounts.models import Customer
from django.conf import settings
import braintree


def total_payment(request):
    sum = 0
    cart = request.session.get('cart')
    products = Product.get_product_by_id(list(request.session.get('cart').keys()))
    for i in products:
        sum += i.price
    return sum

class CheckOut(View):
    def get(self,request):
        gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)
        customer = request.session.get('customer')
        # cart = {'product':quantity}, get quantity from cart object
        cart = request.session.get('cart')
        print(cart.keys())
        # get all product ids
        products = Product.get_product_by_id(list(request.session.get('cart').keys()))
        client_token = gateway.client_token.generate()
        return render(request,'checkout.html',{'products':products, 'client_token':client_token})        


    def post(self,request):
        # instantiate Braintree payment gateway
        gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)
        # address = request.POST.get('address')
        # phone = request.POST.get('phone')
        # transaction_id = request.POST.get('transaction')
        # get customer id from session
        customer = request.session.get('customer')
        # cart = {'product':quantity}, get quantity from cart object
        cart = request.session.get('cart')
        # get all product ids
        products = Product.get_product_by_id(list(request.session.get('cart').keys()))
        total = total_payment(request)
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale ({
            'amount': f'{total}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
        # iterate all product to get price and to create order object
            for product in products:
                order = Order(
                    # must pass customer object due to foreign key relation
                    # create customer object
                    customer = Customer(id = customer),
                    product = product,
                    price = product.price,
                    # address = address,
                    # phone = phone,
                    quantity = cart.get(str(product.id)),
                    paid = True,
                    braintree_id = result.transaction.id
                )
            order.placeOrder()
            # after order is placed, clear the cart
            request.session['cart'] = {}
            return redirect("store:cart")
        else:
            return HttpResponse("<h1>Failed</h1>")


