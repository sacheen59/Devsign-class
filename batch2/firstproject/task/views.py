from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based views (ui)

def index(request):
    return HttpResponse("hello we are learning django")

def second_index(request):
    return HttpResponse("this is second page")

# class based views (api)
