from django.db import models
from django.conf import settings

# Model
from App_Shop.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    item = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cupon=models.BooleanField(default=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart_seller_name",null=True)
    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        if self.cupon:
            total = (self.item.price - (self.item.price * (self.item.cupon_offer/100))) * self.quantity 
            float_total = format(total, '0.2f')
            return float_total
        else:
            total = self.item.price * self.quantity 
            float_total = format(total, '0.2f')
            return float_total

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_seller_name",null=True)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
