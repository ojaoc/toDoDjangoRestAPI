from api.models import Task
from api.serializers import RequestDeleteSeveralSerializer, TaskSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskList(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(detail=False, methods=["post"])
    def delete_several(self, request):
        serializer = RequestDeleteSeveralSerializer(data=request.data)
        if serializer.is_valid():
            Task.objects.filter(pk__in=serializer.data["task_ids"]).delete()
            return Response("Items successfully deleted")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
