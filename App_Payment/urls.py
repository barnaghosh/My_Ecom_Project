from django.urls import path
from App_Payment import views

app_name = "App_Payment"

urlpatterns = [
    path('checkout/<pk>/', views.checkout, name="checkout"),
    path('pay/<pk>/', views.payment, name="payment"),
    path('status/', views.complete, name="complete"),
    path('purchase/<val_id>/<tran_id>/<str:seller>/', views.purchase, name="purchase"),
    path('orders/', views.order_view, name="orders"),
]
