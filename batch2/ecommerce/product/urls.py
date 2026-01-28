from django.urls import path
from . import views

urlpatterns = [
   path('',views.product_page),
   path('categories/',views.get_all_cateogries),
]