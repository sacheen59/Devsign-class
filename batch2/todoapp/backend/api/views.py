from .models import Task
from api.serailzers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Http404
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView, UpdateAPIView,CreateAPIView

"""
class based views:
1. APIView => it is the view which have different method for handling http request, get, put, post, patch, delete
2. Generic View => ListAPIView, CreateAPIView, RetriveAPIView, UpdateAPIView, DeleteAPIView
"""

class TodoView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'

# class CreateTodoView(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class ListCreateTodoAPIView(APIView):

#     def get(self,request,*args,**kwargs):
#         todos = Task.objects.all()
#         serializer = TaskSerializer(todos, many =True)
#         return Response(serializer.data, status=200)

#     def post(self,request,*args,**kwargs):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET','POST'])
# def list_todo(request):
#     if request.method == 'GET':
#         todos = Task.objects.all()
#         serializer = TaskSerializer(todos, many=True)
#         return Response(serializer.data, status=200)

#     if request.method == 'POST':
#         serializer = TaskSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# class TodoDetailView(APIView):

#     def get_object(self, task_id):
#         try:
#             return Task.objects.get(pk=task_id)
#         except Task.DoesNotExist:
#             raise Http404

#     def get(self,request,task_id,*args,**kwargs):
#         task = self.get_object(task_id)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     def put(self,request,task_id,*args,**kwargs):
#         task = self.get_object(task_id)
#         serializer = TaskSerializer(task, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)

#     def patch(self,request,task_id,*args,**kwargs):
#         task = self.get_object(task_id)
#         serializer = TaskSerializer(task, data = request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)

#     def delete(self,request,task_id,*args,**kwargs):
#         task = self.get_object(task_id)
#         task.delete()
#         return Response({'message': 'Task deleted successfully'})





# @api_view(['GET','PUT','DELETE','PATCH'])
# def todo_detail(request,task_id):
#     if request.method == 'GET':
#         """This method is use to retrive the single data."""
#         try:
#             task = Task.objects.get(id = task_id)
#         except Task.DoesNotExist:
#             return Response({'message': "Task with given id doesnot exists"},status=404)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         """This method use to update the data."""
#         try:
#             todo = Task.objects.get(id=task_id)
#         except Task.DoesNotExist:
#             return Response({'message':'Task with given id doesnot exist.'}, status=404)
#         serializer = TaskSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     if request.method == 'PATCH':
#         try:
#             todo = Task.objects.get(id=task_id)
#         except Task.DoesNotExist:
#             return Response({'message':'Task with given id doesnot exist.'}, status=404)
#         serializer = TaskSerializer(todo, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         """This is use to delete the data."""
#         try:
#             todo = Task.objects.get(id=task_id)
#         except Task.DoesNotExist:
#             return Response({'message':'Task with given id doesnot exist.'}, status=404)
#         todo.delete()
#         return Response({'message': 'Task deleted succesfully.'})