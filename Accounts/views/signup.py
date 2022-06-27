from django.shortcuts import render, redirect
from Accounts.forms import CustomerForm
from django.contrib import messages
from django.views import View

# Create your views here.

class SignUp(View):

    def get(self,request):
        form = CustomerForm()
        return render(request,'signup.html',{'form':form})
        

    def post(self,request):
        form = CustomerForm(request.POST)
        # In the 'form' class the clean function is defined, if all the data is correct,as per the clean function, it returns true
        if form.is_valid(): 
            first_name= form.cleaned_data.get('first_name')
            form.save()
            messages.success(request,f"Account for {first_name} successfully created.")
            return redirect('store:index')

