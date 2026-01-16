from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based views (ui)

def index(request):
    
    return render(request,'task/index.html',{
        "title": "My first page",
        "description": "This is my first page description",
        "page_no": 1,
    })

def second_index(request):
    return render(request,'task/second-page.html')

def third_page(request):
    return HttpResponse("This is third page")

# class based views (api)
