from django.urls import path
from . import views

urlpatterns = [
   path('',views.product_page,name='product_page'),
   path('categories/',views.get_all_cateogries,name='all_categories'),
   path('delete-category/<int:category_id>/',views.delete_category,name='delete_category')
]