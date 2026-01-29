from django.shortcuts import render,redirect
from .models import Product,Category
from django.http import HttpResponse

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

def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('all_categories')

# def dynamic_url(request,category_id):
#     return HttpResponse(f"dynamic url ===> {category_id}")
