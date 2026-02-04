from django.shortcuts import render,redirect
from .models import Product,Category
from django.http import HttpResponse

# Create your views here.

def product_page(request):
    products = Product.objects.all()
    return render(request, 'product/product-page.html',{
        'products': products,
        "product_length": len(products) > 0
    })

def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_page')

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

def form_practise(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("email ====> ",email)
        print("password====> ",password)
    return render(request,'product/login-form.html')