from django.shortcuts import redirect
from django.contrib import messages
 
def logout(request):
    request.session.clear()
    messages.success(request,f"Logout Successful")
    return redirect('store:index')