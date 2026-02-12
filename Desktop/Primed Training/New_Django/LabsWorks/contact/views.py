from django.shortcuts import render
from django.http import HttpResponse

def contact (request):
    return HttpResponse ("Contact: This is the contact page.")
def ceo (request):
    return HttpResponse ("CEO: Ina is the CEO of our company and She is doing well.")
