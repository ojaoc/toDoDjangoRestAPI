from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("create-task/", views.create_task),
    path("update-task/<str:pk>", views.update_task),
    path("delete-task/<str:pk>", views.delete_task),
    path("list-tasks/", views.list_tasks),
    path("get-single-task/<str:pk>", views.get_single_task),
]
