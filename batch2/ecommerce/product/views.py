from django.shortcuts import render
from .models import Product

# Create your views here.

def product_page(request):
    products = Product.objects.all()
    return render(request, 'product/product-page.html',{
        'products': products
    })
