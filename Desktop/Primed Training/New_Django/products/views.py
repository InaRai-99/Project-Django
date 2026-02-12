from django.shortcuts import render
from django.http import HttpResponse

def add (request):
    return HttpResponse ("Add: Add the products here")
def delete (request):
    return HttpResponse ("Delete: The product")
def update (request):
    return HttpResponse ("Update: Update your basket.")
def checkout(request):
    return HttpResponse ("Checkout: Checkout your products.")
# Create your views here.


