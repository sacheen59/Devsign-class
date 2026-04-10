from django.urls import path
from . import views

urlpatterns = [
    # path('list/',views.list_todo),
    # path('list/',views.ListCreateTodoAPIView.as_view()),
    path('list/',views.TodoView.as_view()),
    # path('create/',views.CreateTodoView.as_view()),
    # path('detail/<int:task_id>/',views.todo_detail)\
    path('detail/<int:task_id>/',views.TodoDetailView.as_view())
]