from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('second-page/',views.second_index),
    path('third-page/',views.third_page),
]
