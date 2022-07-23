from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib import messages
 
def logout(request):
    customer = request.session.get('customer')
    if customer != None:
        request.session.clear()
        messages.success(request,f"Logout Successful")
        return redirect('store:index')
    else:
        messages.error(request,"You are not logged in")
        return redirect('store:index')
