from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)
    seller=models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_cat',null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    # seller=models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_name')
    seller=models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    mainimage = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    cupon_number=models.CharField(max_length=100,blank=True,null=True)
    cupon_offer=models.PositiveIntegerField(default=0,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]
