from Accounts.models import Customer
from django.views import View
from django.shortcuts import redirect, render
from Accounts.forms import UpdateProfileForm
from django.contrib import messages


class UpdateProfile(View):
    def get(self,request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id = customer_id)
        initial_dict = {
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'phone':customer.phone,
            'address':customer.address,
            'email':customer.email
        }
        form = UpdateProfileForm(initial=initial_dict)
        return render(request,'update_profile.html')

    def post(self,request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id = customer_id)
        form = UpdateProfileForm(request.POST, instance = customer, initial = customer.data)
        if form.is_valid():
            form.save()
            messages.success('Profile Updated Successfully')
            return redirect('account:profile')
        else:
            messages.error('Error in updating profile')
        context = {'form':form}
        return render(request,'update_profile.html',context)

