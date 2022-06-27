from django.shortcuts import render
from Store.models import *
from django.views import View

# Create your views here.
class IndexView(View):
    
    def get(self,request):
        data = {}
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
        return render(request,'index.html',data)
    