from django.shortcuts import render

# Create your views here.

def SignUp(request):
    return render(request,'signup.html')