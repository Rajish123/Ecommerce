from django.shortcuts import render
from Store.models import Product
from django.views import View


class HomeView(View):
    def get(self,request):
        products = Product.get_all_products()
        return render(request,'home.html',{'products':products})