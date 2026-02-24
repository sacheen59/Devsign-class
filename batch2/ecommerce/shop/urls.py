from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('all_products/',views.get_all_products, name="product-page"),
    path('<int:product_id>/',views.get_individual_product, name="single-product"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.cart_page,name="cart-page"),
    path('cart_delete/<int:cart_id>/',views.cart_delete,name='delete-cart')
]

#localhost:8000