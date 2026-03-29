import uuid
import json
import base64

from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart,Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from django.urls import reverse

from django.views import View
from shop.generate_signature import genSha256

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
              return redirect(f'{reverse('esewa_form')}?o_id={str(order.id)}&c_id={str(cart_item.id)}')
            # /esewa/form?o_id=1&c_id=2&user=amisha


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


class EsewaView(View):
    def get(self,request,*args,**kwargs):
        o_id = request.GET.get('o_id')
        c_id = request.GET.get('c_id')
        cart = Cart.objects.get(id=int(c_id))
        order = Order.objects.get(id=int(o_id))

        uuid_val = uuid.uuid4()

        secret_key = "8gBm/:&EnhH.1/q"
        data_to_sign = f"total_amount={order.total_price},transaction_uuid={uuid_val},product_code=EPAYTEST"
        signature = genSha256(secret_key,data_to_sign)

        data = {
            'amount': order.product.product_price,
            'total_amount': order.total_price,
            'transaction_uuid': uuid_val,
            'product_code': 'EPAYTEST',
            'signature': signature
        }

        return render(request,'shop/esewaform.html',{
            'order':order,
            'cart': cart,
            'data': data
        })



@login_required
def esewa_verify(request,order_id,cart_id):
    data = request.GET.get('data')
    decoded_data = base64.b64decode(data).decode('utf-8')
    map_data = json.loads(decoded_data)
    order = Order.objects.get(id=order_id)
    cart = Cart.objects.get(id=cart_id)

    if map_data.get('status') == 'COMPLETE':
        order.payment_method = 'paid'
        order.save()
        cart.delete()

    return redirect('order-page')