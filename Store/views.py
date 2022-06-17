from math import prod
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Index(request):
    data = {}
    products = None
    categories = Category.get_all_categories()
    # read string from url/server inthis case /?category = categoryId
    # read data that is passed to server
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html',data)
