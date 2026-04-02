from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list_todo),
    path('detail/<int:task_id>/',views.todo_detail)
]