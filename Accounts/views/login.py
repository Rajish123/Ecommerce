from django.shortcuts import render, redirect
from django.contrib import messages
from Accounts.models import Customer
from django.contrib.auth.hashers import check_password
from django.views import View



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
                # save user information in session after logging in
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                # print(request.session.get('email'))
                # successful logged in
                messages.success(request,f"Login Successful")
                return redirect('store:index')
            else:
                messages.info(request,f"Email or Password Invalid !")
        else:
            messages.info(request,f"Account not found with given email.")
        return render(request,'login.html')
        

