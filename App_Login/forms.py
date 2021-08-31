from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import transaction

from .models import Buyer,Seller,User,Profile

class BuyerSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_buyer = True
        user.save()
        buyer = Buyer.objects.create(user=user)
        return user


class SellerSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))
    phone=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Enter phone number'}))
    
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('email','username','password1','password2','phone',)
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)
        seller.phone=self.cleaned_data.get('phone')
        seller.save()

        return user


class Login_form(AuthenticationForm):
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model=User
        fields=('username','password')

class EditProfile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=Profile()
        exclude=('user',)