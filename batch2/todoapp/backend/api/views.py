from django.http import JsonResponse
from .models import Task
from api.serailzers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
