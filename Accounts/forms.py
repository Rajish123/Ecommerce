from asyncore import read
from django import forms
from django.forms import ModelForm
from Accounts.models import Customer
from django.contrib.auth.hashers import make_password

class CustomerForm(ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('first_name','last_name','address','phone','email','password1','password2')
        widgets={
            'first_name': forms.TextInput(attrs={'class':'asd', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'asd', 'placeholder':'Last Name'}),
            'address': forms.TextInput(attrs={'class':'asd', 'placeholder':'Address'}),
            'phone': forms.TextInput(attrs={'class':'asd', 'placeholder':'Phone Number'}),
            'email': forms.EmailInput(attrs={'class':'asd', 'placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class':'asd', 'placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'class':'asd', 'placeholder':'Password'}),


    }



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

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

    def save(self, commit=True):

        new_password = self.clean_password2()
        customer = super(CustomerForm, self).save(commit=False)
        customer.password = make_password(new_password)
        if(commit):
            customer.register()

        return customer