from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib import messages
from .models import Customer
from django.contrib.auth.hashers import check_password

# Create your views here.

def SignUp(request):
    context = {}
    if request.method == "POST":
        form = CustomerForm(request.POST)
        # In the 'form' class the clean function is defined, if all the data is correct,as per the clean function, it returns true
        if form.is_valid(): 
            first_name= form.cleaned_data.get('first_name')
            form.save()
            messages.success(request,f"Account for {first_name} successfully created.")
            return redirect('store:index')
    else:
        form = CustomerForm()
    context['form'] = form
    return render(request,'signup.html',context)

def Login(request):
    # context = {}
    if request.method == "POST":
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
    else:
        return render(request,'login.html')
    return render(request,'login.html')