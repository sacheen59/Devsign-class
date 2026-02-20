from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('all_products/',views.get_all_products, name="product-page"),
    path('<int:product_id>/',views.get_individual_product, name="single-product"),
    path('cart/',views.cart_page,name="cart-page"),
]

#localhost:8000