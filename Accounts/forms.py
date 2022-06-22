from django import forms
from django.forms import ModelForm
from Accounts.models import Customer
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.hashers import make_password

class CustomerForm(ModelForm):

    first_name = forms.CharField(max_length='20')
    last_name = forms.CharField(max_length='20')

    phone = PhoneNumberField(required = True)
    email = forms.EmailField(required = True,widget=forms.EmailInput)
    password = forms.CharField(max_length=15, min_length=4,widget=forms.PasswordInput)



    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone','email','password']



        # this function will be used for the validation
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')


        if not first_name:
            raise forms.ValidationError("First name required!")

        elif len(first_name) < 4:
            raise forms.ValidationError('First Name must be 4 char long or more')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise forms.ValidationError('Last Name Required')
        if len(last_name) < 4:
            raise forms.ValidationError('Last Name must be 4 char long or more')

        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        return email

    def save(self, commit=True):

        customer = super(CustomerForm, self).save(commit=False)
        customer.password = make_password(customer.password)
        # customer.set_password(self.cleaned_data['password1'])
        if(commit):
            customer.register()

        return customer