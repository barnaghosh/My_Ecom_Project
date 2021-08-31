from django.urls import path
from App_Shop import views

app_name='App_Shop'

urlpatterns = [
    path('create_title/',views.create_category,name='catagory'),
    path('add_product/<int:pk>/',views.create_product,name='add_product'),
    path('add_another_product/',views.create_another_product,name='add_another_product'),
    path('',views.Home.as_view(),name='home_product'),
    path('product_details/<int:pk>/',views.ProductDetail.as_view(),name='product_detail'),
]
