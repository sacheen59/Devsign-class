from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def todos(request):
    todos = [
        {
            'id': 1,
            'task': "Learn Django for 20 minutes.",
            'isCompleted': True,
        },
        {
            'id': 2,
            'task': "Run for 10 minutes.",
            'isCompleted': False,
        },
        {
            'id': 3,
            'task': "Explore React.",
            'isCompleted': False,
        },
        {
            'id': 4,
            'task': "Go and buy a coffee.",
            'isCompleted': True,
        },
    ]
    return Response(todos)
