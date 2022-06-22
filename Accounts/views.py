from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib import messages

# Create your views here.

def SignUp(request):
    context = {}
    if request.method == "POST":
        form = CustomerForm(request.POST)
        # In the 'form' class the clean function is defined, if all the data is correct,as per the clean function, it returns true
        if form.is_valid(): 
            first_name= form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Account for {first_name} successfully created.")
            return redirect('store:index')
    else:

        form = CustomerForm()
    context['form'] = form
    return render(request,'signup.html',context)