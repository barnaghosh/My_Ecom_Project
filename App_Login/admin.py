from django.contrib import admin
from App_Login.models import User,Seller,Buyer,Profile

# Register your models here.
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Profile)
