from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField()
    is_completed = serializers.BooleanField()

    def create(self, validated_data):
        # task = validated_data.get('task')
        # is_completed = validated_data.get('is_completed')
        return Task.objects.create(**validated_data)