from django.shortcuts import render
from django.http import HttpResponse

def about (request):
    return HttpResponse ("About us: This is our first view of the app pages.")
def ceo (request):
    return HttpResponse ("CEO: Ina is the CEO of our company and ...")
# Create your views here.
