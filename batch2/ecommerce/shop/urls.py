from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('<int:product_id>/',views.get_individual_product, name="single-product")
]

#localhost:8000