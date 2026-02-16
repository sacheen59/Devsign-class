from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

def home_page(request):
    products = Product.objects.all().order_by('-id')[:8]
    return render(request, 'shop/homepage.html',{'products': products})
