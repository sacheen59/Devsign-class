from django.urls import path
from . import views

urlpatterns = [
   path('',views.ProductPageView.as_view(),name='product_page'),
   path('add-product/',views.CreateProductView.as_view(),name='add_product'),
   path('edit-product/<int:product_id>/',views.edit_product, name='edit_product'),
   path('<int:pk>/',views.DeleteProductView.as_view(),name='delete_product'),
   path('categories/',views.get_all_cateogries,name='all_categories'),
   path('delete-category/<int:category_id>/',views.delete_category,name='delete_category'),
   path('login-form/',views.form_practise, name='login-form')
]