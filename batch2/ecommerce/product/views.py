from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Product,Category,LoginPractise
from product.forms import LoginForm,ProductForm,EditProductForm
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


# class based views
class ProductPageView(ListView):
    """class based views for product page."""
    model = Product
    template_name = 'product/product-page.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        return {
            'products': products,
            'product_length': len(products) > 0
        }
    # def get(self,request):
    #     products = Product.objects.all()
    #     return render(request, 'product/product-page.html', {
    #         'products': products,
    #         'product_length': len(products) > 0
    #     })


# def product_page(request):
#     products = Product.objects.all()
#     return render(request, 'product/product-page.html',{
#         'products': products,
#         "product_length": len(products) > 0
#     })


class CreateProductView(CreateView):
    """Class based view to create the product"""
    # def get(self,request):
    #     form = ProductForm()
    #     return render(request, 'product/product-form.html',{'form': form})

    # def post(self,request):
    #     form = ProductForm(data=request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('product_page')
    model = Product
    template_name = 'product/product-form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_page')

def post_product(request):
    """Method to add/create the product."""
    if request.method == 'POST':
        form = ProductForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_page')
    else:
        form = ProductForm()
    return render(request,'product/product-form.html',{'form': form})


def edit_product(request,product_id):
    "Method to edit the product data."
    product = Product.objects.get(id = product_id)
    if request.method == "POST":
        form = EditProductForm(data=request.POST,files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_page')
    else:
        form = EditProductForm(instance=product)
    return render(request, "product/edit-product.html",{'form': form})


class DeleteProductView(DeleteView):
    """Class based views to delete the product"""
    model = Product
    success_url = reverse_lazy('product_page')
    template_name = 'product/confirm_delete.html'


def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_page')


def get_all_cateogries(request):
    categories = Category.objects.all()
    return render(request, 'product/categories.html',{
        'categories': categories
    })

# post category

# edit category


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
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request,'product/login-form.html',{'form': form})