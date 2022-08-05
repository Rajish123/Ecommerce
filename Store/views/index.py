from cmath import e
from django.shortcuts import redirect, render
from Store.models import *
from django.views import View

# Create your views here.
class IndexView(View):
    # to handle add to cart
    def post(self,request):
        # can access only if name is specified in form
        # get product id from server which was send by user through add to cart
        # return product id
        product = request.POST.get('product')
        # if user wants to deduct product from cart
        remove = request.POST.get('remove')
        # access cart object from session
        # cart stored as dictionary
        cart = request.session.get('cart')
        # if cart in session, appends product in cart
        if cart:
            # check if product is already in cart
            # here product id is passed, we get quantity
            quantity = cart.get(product)
            if quantity:
                if remove:
                    # if quantity = 0 then remove product from cart
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            # assigns empty dictionary
            cart = {}
            cart[product] = 1

        # stores cart object in session
        request.session['cart'] = cart
        print(product)
        print(f"cart {request.session['cart']}")
        return redirect('store:index')
    
    def get(self,request):
        data = {}
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        # read string from url/server inthis case /?category = categoryId
        # read data that is passed to server
        # get from query string.Here get data from /?category=
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data['products'] = products
        data['categories'] = categories
        # print the user information that is stored in session after logging in.
        # print(f"The current user is {request.session.get('email')}")
        return render(request,'index.html',data)
    