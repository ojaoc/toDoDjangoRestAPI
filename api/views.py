from api.models import Task
from api.serializers import TaskSerializer
from rest_framework import viewsets

class TaskList(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()