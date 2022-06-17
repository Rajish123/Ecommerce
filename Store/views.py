from math import prod
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Index(request):
    product = Product.get_all_products()
    return render(request,'index.html',{'product':product})
