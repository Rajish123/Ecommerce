from django.views import View
from Accounts.models import Customer
from django.shortcuts import render

class Profile(View):
    def get(self,request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id = customer_id)
        cart = request.session.get('cart').keys()
        print(f"total items = {len(cart)}")
        context = {'customer':customer}
        return render(request,'profile.html',context)


