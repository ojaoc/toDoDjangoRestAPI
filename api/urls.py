from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("create-task/", views.create_task),
    path("update-task/", views.update_task),
    path("delete-task/", views.delete_task),
    path("list-tasks/", views.list_tasks),
    path("get-single-task/<str:pk>", views.get_single_task),
]
