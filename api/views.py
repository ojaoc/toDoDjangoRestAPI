from api.models import Task
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return Response(f"Task with id '{pk}' successfully deleted.")


@api_view(["GET"])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_single_task(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)
