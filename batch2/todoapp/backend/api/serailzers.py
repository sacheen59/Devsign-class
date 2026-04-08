from rest_framework import serializers
from .models import Task

"""
type of validation:
1. Field level validation => validate_<field_name>(self,value: type of data)
2. Object level validation => validate(self,attrs: dict)
3. custom validators
"""

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField()
    description = serializers.CharField()

    def to_internal_value(self, data):
        """It is use to deserialize the data"""
        print("to internal value called")
        return super().to_internal_value(data)


    def validate_task(self,value):
        print("field level validation called")
        if len(value) < 3:
            raise serializers.ValidationError("The task must be more than 3 characters.")
        return value

    def validate(self, attrs):
        print("To validate method called")
        task = attrs.get('task')
        if Task.objects.filter(task=task).exists():
            raise serializers.ValidationError("This task is already exists")
        return {
            "data" : attrs,
            "course": "python"
        }

    def create(self, validated_data):
        """when data is created."""
        # task = validated_data.get('task')
        # is_completed = validated_data.get('is_completed')
        print("Create method called")
        print("validated_data ===> ", validated_data)
        data = validated_data.get('data')
        return Task.objects.create(**data)

    def update(self, instance, validated_data):
        """When data is updated."""
        print("update method called")
        data = validated_data.get('data')
        instance.task = data.get('task', instance.task)
        # instance.is_completed = validated_data.get('is_completed',instance.is_completed)
        instance.save()
        return instance

    def to_representation(self, instance):
        print("To representation called.")
        data = super().to_representation(instance)
        task = data.get('task')
        data['task_in_uppercase'] = task.upper()
        return data

"""
GET => to_representation
POST => to_internal_values, validate_<field_name>, validate, create
PUT, PATCH => to_internal_values, validate_<field_name>, validate, update
"""

