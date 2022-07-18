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


def checkout_page(request):
    # generate all other required data that you may need on the checkout page and add them to context
    # if settings.BRAINTREE_PRODUCTION:
    #     braintree_env = braintree.Environment.Production
    # else:
    braintree_env = braintree.Environment.Sandbox

    # configure braintree
    braintree.Configuration.configure(
        braintree_env,
        merchant_id = settings.BRAINTREE_MERCHANT_ID,
        public_key = settings.BRAINTREE_PUBLIC_KEY,
        private_key = settings.BRAINTREE_PRIVATE_KEY,
    )
    try:
        braintree_client_token = braintree.ClientToken.generate({"customer_id":Customer.id})
    except:
        braintree_client_token = braintree.ClientToken.generate({})
    context = {'braintree_client_token':braintree_client_token}
    return render(request,'checkout.html',context)


def payment(request):
    nonce_from_the_client = request.POST['paymentMethodNonce']
    customer_kwargs = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }
    customer_create = braintree.Customer.create(customer_kwargs)
    customer_id = customer_create.customer.id
    result = braintree.Transaction.sale({
        "amount": total_payment(),
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    print(result)
    return HttpResponse('Ok')


class CheckOut(View):
    def get(self,request):
        customer = request.session.get('customer')
        # cart = {'product':quantity}, get quantity from cart object
        cart = request.session.get('cart')
        print(cart.keys())
        # get all product ids
        products = Product.get_product_by_id(list(request.session.get('cart').keys()))
        return render(request,'cart.html',{'products':products})        


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


