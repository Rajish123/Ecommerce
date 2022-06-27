from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib import messages
from .models import Customer
from django.contrib.auth.hashers import check_password
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

class Login(View):

    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        # get password from login form
        password = request.POST.get('password')
        # get customer from provided email
        customer = Customer.get_customer_by_email(email)
        if customer:
            # checks hashed password with real password
            # Here, Customer.password is encoded password saved in database
            flag = check_password(password,customer.password)
            # if password provided in login form matched with password in database returns True
            if flag:
                # successful logged in
                messages.success(request,f"Login Successful")
                return redirect('store:index')
            else:
                messages.info(request,f"Email or Password Invalid !")
        else:
            messages.info(request,f"Account not found with given email.")

