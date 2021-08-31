from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Shop.forms import CatagoryForm,ProductForm,ProductFormAnother
from App_Shop.models import Category,Product
from App_Login.models import Seller
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
# Create your views here.

# class CreateQuiz(CreateView):
#     fields=('course_name','question_number',)
#     model=category
#     template_name='quiz/create.html'
#     def get_success_url(self):
#         print('pk')
#         print(self.get_object)
def is_seller(user):
    try:
        return user.is_authenticated and user.seller is not None
    except Seller.DoesNotExist:
        return False
@user_passes_test(is_seller)
def create_product(request,pk):
    category=Category.objects.get(pk=pk)
    form=ProductFormAnother()
    if 'save' in request.POST:
        form=ProductFormAnother(request.POST,request.FILES)
        # print(form)
        # check=Category.objects.filter(title=form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.category=category
            form.save()
            return HttpResponseRedirect(reverse('App_Login:home'))
    if 'another' in request.POST:
        form=ProductFormAnother(request.POST,request.FILES)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.category=category
            form.save()
            return HttpResponseRedirect(reverse('App_Shop:add_product',kwargs={'pk':pk}))
    return render(request,'quiz/create_ans.html',context={'form':form})

@user_passes_test(is_seller)
def create_category(request):
    form=CatagoryForm()
    if request.method == 'POST':
        form=CatagoryForm(request.POST)
        
        if form.is_valid():
            
            form=form.save(commit=False)
            print('test1')
            print(form)
            check=Category.objects.filter(title=form)
            print('check')
            print(check)
            if check:
                messages.info(request, "This catagory is already added please go to Add product in catagory.")
                return HttpResponseRedirect(reverse('App_Shop:home_product'))
            else:  
                form.seller=request.user
                form.save()
                pk=form.pk
                print('test2')
                print(form)
                return HttpResponseRedirect(reverse('App_Shop:add_product',kwargs={'pk':pk}))
    return render(request,'quiz/create.html',context={'form':form})



@user_passes_test(is_seller)
def create_another_product(request):
    
    form=ProductForm()
    if 'save' in request.POST:
        form=ProductForm(request.POST,request.FILES)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.save()
            return HttpResponseRedirect(reverse('App_Login:home'))
    if 'another' in request.POST:
        form=ProductForm(request.POST,request.FILES)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.save()
            return HttpResponseRedirect(reverse('App_Shop:add_another_product'))
    return render(request,'quiz/create_ans.html',context={'form':form})

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'