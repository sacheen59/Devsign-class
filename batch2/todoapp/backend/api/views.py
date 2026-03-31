from django.http import JsonResponse
from .models import Task

def list_todo(request):
    todos = Task.objects.all()
    return JsonResponse({'todos': todos})