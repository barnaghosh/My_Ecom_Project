from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.urls import reverse

# Authentications
from django.contrib.auth.decorators import login_required

# Model
from App_Order.models import Cart, Order
from App_Shop.models import Product
from App_Login.models import User
# Messages
from django.contrib import messages
# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print("Item")
    print(item.seller)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False,seller=item.seller)
    print("Order Item Object:")
    print(order_item)
    print(order_item[0])
    order_qs = Order.objects.filter(user=request.user,seller=item.seller , ordered=False)
    print("Order Qs:")
    print(order_qs)
    #print(order_qs[0])
    if order_qs.exists():
        order = order_qs[0]
        print("If Order exist")
        print(order)
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated.")
            return redirect("App_Shop:home_product")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart.")
            return redirect("App_Shop:home_product")
    else:
        order = Order(user=request.user)
        order.seller=item.seller
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart.")
        return redirect("App_Shop:home_product")


@login_required
def cart_view(request):
    users=User.objects.all()
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    print('order')
    print(orders)
    if carts.exists() and orders.exists():
        order = orders
        return render(request, 'App_Order/cart1.html', context={'carts':carts, 'orders':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect("App_Shop:home_product")

      
    
    


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user,seller=item.seller, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed form your cart")
            return redirect("App_Order:cart")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("App_Shop:home_product")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_Shop:home_product")

@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user,seller=item.seller, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print('item')
        print(order)
        
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("App_Shop:home_product")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_Shop:home_product")


@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user,seller=item.seller, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_Order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} item has been removed from your cart")
                return redirect("App_Order:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("App_Shop:home_product")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_Shop:home_product")

@login_required
def cupon(request,pk):
    item = get_object_or_404(Product, pk=pk)
    carts=Cart.objects.filter(item=item,seller=item.seller,user=request.user,cupon=False)
    print(carts)
    if carts.exists():
        if request.method == "GET":
            search=request.GET.get('cupon','')
            result=Product.objects.filter(cupon_number=search,pk=pk)
            print('cupon')
            print(search)
            if search != '':
                if item.cupon_number == search:
                
                    for cart in carts:
                            cart.cupon=True
                            cart.save()
                            messages.info(request,'Cupon feature is Applied')
                            return redirect('App_Order:cart') 
                else:
                    messages.info(request,'Cupon number is not match')
                    return HttpResponseRedirect(reverse('App_Order:cupon',kwargs={'pk':pk})) 
            
    else:
        messages.info(request,'Cupon offer already exists')
        return redirect('App_Order:cart')
    return render(request,'App_Order/cupon.html',context={'item_cupon':item.cupon_number,'search':search})

@login_required
def add_cupon(request,search,pk):
    item = get_object_or_404(Product, pk=pk)
    result=Product.objects.filter(cupon_number=search,pk=pk)
    carts=Cart.objects.filter(item=item,seller=item.seller,user=request.user,cupon=False)
   
    if carts.exists():
        if result:
            for cart in carts:
                cart.cupon=True
                cart.save()
                messages.info(request,'Cupon feature Applied')
                return redirect('App_Order:cart') 
        else:
            messages.info(request,'Cupon is wrong')
            return HttpResponseRedirect(reverse('App_Order:cart'))
    else:
        messages.info(request,'Cupon offer already exists')
        return redirect('App_Order:cart')

@login_required
def cupon1(request,pk):
    item = get_object_or_404(Product, pk=pk)
    carts=Cart.objects.filter(item=item,seller=item.seller,user=request.user,cupon=False)
    print(carts)
   
    if request.method == "GET":
        search=request.GET.get('cupon','')
        result=Product.objects.filter(cupon_number=search,pk=pk)
        print('cupon')
        print(result)
        return HttpResponseRedirect(reverse('App_Order:cupon_check',kwargs={'search':search,'pk':pk}))
         
            
    
    return render(request,'App_Order/cupon.html',context={})
