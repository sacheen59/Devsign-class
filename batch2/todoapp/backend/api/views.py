from django.http import JsonResponse
from .models import Task
from api.serailzers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def get_object_or_error(model_name, id, serializer):
    try:
        data = model_name.objects.get(id=id)
    except model_name.DoesNotExists:
        return Response({'message': 'no data found'}, status=404)
    return data



@api_view(['GET','POST'])
def list_todo(request):
    if request.method == 'GET':
        todos = Task.objects.all()
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def todo_detail(request,task_id):
    if request.method == 'GET':
        """This method is use to retrive the single data."""
        data = get_object_or_error(Task,task_id)
        serializer = TaskSerializer(data)
        return Response(serializer.data)

    if request.method == 'PUT':
        """This method use to update the data."""
        try:
            todo = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'message':'Task with given id doesnot exist.'}, status=404)
        serializer = TaskSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        """This is use to delete the data."""
        try:
            todo = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'message':'Task with given id doesnot exist.'}, status=404)
        todo.delete()
        return Response({'message': 'Task deleted succesfully.'})