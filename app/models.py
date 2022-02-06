"""
Create ToDo model
"""
from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    """
    ToDo Model Attributes
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    end_user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    due_date = models.DateTimeField()
