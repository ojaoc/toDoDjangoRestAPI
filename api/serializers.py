from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class RequestDeleteSeveralSerializer(serializers.Serializer):
    task_ids = serializers.ListField()
