from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description

    class Meta:
        ordering = ["is_done"]
