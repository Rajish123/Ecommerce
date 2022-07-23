from Accounts.models import *
from Accounts.forms import ChangePasswordForm
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password


class ChangePassword(View):

    def get(self,request):
        form = ChangePasswordForm()
        return render(request,'change_password.html',{'form':form})
        

    def post(self,request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id = customer_id)
        oldPassword = customer.password
    
        old_password = request.POST.get('old_password')
        password_check = check_password(old_password,oldPassword)
        form = ChangePasswordForm(request.POST, instance=customer)

        if password_check:
            # In the 'form' class the clean function is defined, if all the data is correct,as per the clean function, it returns true
            if form.is_valid(): 
                form.save()
                messages.success(request,f"Password Changed Successfully.")
                return redirect('store:home')
        else:
            messages.success(request,f"Password  Not Changed Successfully.")

        return render(request,'change_password.html',{'form':form})
        