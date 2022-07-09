from django.shortcuts import render
from django.views import View

class AboutView(View):
    def get(self,request):
        return render(request,'about.html')