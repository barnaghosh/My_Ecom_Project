from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse


def main(request):
    return HttpResponseRedirect(reverse('App_Login:home'))