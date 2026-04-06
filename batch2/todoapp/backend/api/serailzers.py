from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField()

    def to_internal_value(self, data):
        return super().to_internal_value(data)


    def validate(self, attrs):
        print("validated data ==> ", attrs)
        print("To validate method called")
        return super().validate(attrs)

    def create(self, validated_data):
        """when data is created."""
        # task = validated_data.get('task')
        # is_completed = validated_data.get('is_completed')
        print("Create method called")
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """When data is updated."""
        print("update method called")
        instance.task = validated_data.get('task', instance.task)
        # instance.is_completed = validated_data.get('is_completed',instance.is_completed)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        task = data.get('task')
        data['task_in_uppercase'] = task.upper()
        return data