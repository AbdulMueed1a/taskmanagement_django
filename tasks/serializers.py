from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'due_date', 'created_at', 'updated_at', 'user'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def validate_due_date(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError(
                "Due date must be in the future."
            )
        return value

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )
        return value.strip()


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'status', 'priority', 'due_date'
        ]

    def validate_due_date(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError(
                "Due date must be in the future."
            )
        return value


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'status', 'priority', 'due_date'
        ]

    def validate_due_date(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError(
                "Due date must be in the future."
            )
        return value