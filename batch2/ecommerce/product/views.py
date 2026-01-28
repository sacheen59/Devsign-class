from django.shortcuts import render
from .models import Product,Category

# Create your views here.

def product_page(request):
    products = Product.objects.all()
    return render(request, 'product/product-page.html',{
        'products': products
    })

def get_all_cateogries(request):
    categories = Category.objects.all()
    return render(request, 'product/categories.html',{
        'categories': categories
    })
