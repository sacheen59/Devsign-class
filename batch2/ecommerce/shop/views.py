from django.shortcuts import render
from product.models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only

@user_only
def home_page(request):
    products = Product.objects.all().order_by('-id')[:8]
    return render(request, 'shop/homepage.html',{'products': products})

@user_only
def get_all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html',{'products': products})

@user_only
def get_individual_product(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/single-product.html',{'product': product})

@login_required
@user_only
def cart_page(request):
    return HttpResponse("This is cart page of authenticated user")
