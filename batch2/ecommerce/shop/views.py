from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart,Order
from .forms import OrderForm
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
def add_to_cart(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.create(user=user, product= product)
    cart.save()
    return redirect('cart-page')

@login_required
@user_only
def cart_page(request):
    carts = Cart.objects.filter(user = request.user)
    return render(request,'shop/cart-page.html',{'carts': carts,'cart_length': len(carts) > 0})

@login_required
@user_only
def cart_delete(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart-page')


@login_required
@user_only
def order(request,cart_id, product_id):
    cart_item = Cart.objects.get(id=cart_id)
    product = Product.objects.get(id = product_id)
    user = request.user
    if request.method == 'POST':
       form = OrderForm(request.POST)
       if form.is_valid():
            data = form.cleaned_data
            quantity=data['quantity']
            payment_method = data['payment_method']
            # Order placed
            order = Order.objects.create(
                product=product,
                user=user,
                address=data['address'],
                contact_no=data['contact_no'],
                quantity=quantity,
                total_price=quantity*product.product_price,
                payment_method = payment_method
            )
            if order.payment_method == 'esewa':
              pass
            
            return redirect('order-page')
    else:
        form = OrderForm()
    return render(request,'shop/order-form.html',{ 'form': form })


@login_required
@user_only
def my_order_item(request):
    user = request.user
    order_items = Order.objects.filter(user=user)
    return render(request,'shop/order-page.html', {'orders': order_items, 'order_length': len(order_items) > 0})
