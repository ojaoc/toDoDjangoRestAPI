from django.db import models
import datetime


class Task(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description
