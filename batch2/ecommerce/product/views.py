from django.shortcuts import render,redirect
from .models import Product,Category,LoginPractise
from django.http import HttpResponse
from product.forms import LoginForm

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
    # if method == post
    if request.method == 'POST':
        # forms object created and uta form ko post bata input gareko data aayo
        form = LoginForm(data=request.POST)
        # form ko data valid xa kii xaina check gareko
        if form.is_valid():
            # data chai valid xa vaney cleaned_data vanni dictionary maa aawoxa
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # is_admin = form.cleaned_data['is_admin']

            LoginPractise.objects.create(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                is_Admin = form.cleaned_data['is_admin']
            )

    form = LoginForm()
    return render(request,'product/login-form.html',{'form': form})