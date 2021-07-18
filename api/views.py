from django.core.exceptions import ValidationError
from django.http.response import HttpResponseBadRequest
from api.models import Task
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    except ValidationError:
        return Response(ValidationError, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(["PUT"])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            f"Task with pk of {pk} does not exist", status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)

    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    except ValidationError:
        return Response(ValidationError, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            f"Task with pk of {pk} does not exist", status=status.HTTP_404_NOT_FOUND
        )

    task.delete()

    return Response(f"Task with id '{pk}' successfully deleted.")


@api_view(["GET"])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_single_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            f"Task with pk of {pk} does not exist", status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)
