from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

class OptionalSlashRouter(DefaultRouter):

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'

router = OptionalSlashRouter()
router.register("tasks", viewset=views.TaskList)

# URLConf
urlpatterns = [
    path("", include(router.urls))
]
