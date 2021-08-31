from django import forms
from django.db.models import fields
from . import models

class CatagoryForm(forms.ModelForm):
    # title=forms.CharField(label='',widget=fo)
    title=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':' Enter Catagory'}))
    class Meta:
        model=models.Category
        fields=['title',]


class ProductForm(forms.ModelForm):
 
    class Meta:
        model=models.Product
        fields=['category','mainimage','name','preview_text','detail_text','price','old_price','cupon_number','cupon_offer',]
        


class ProductFormAnother(forms.ModelForm):
   
    class Meta:
        model=models.Product
        fields=['mainimage','name','preview_text','detail_text','price','old_price','cupon_number','cupon_offer',]