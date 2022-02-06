"""
creating serializers which will handle all operations
for ToDo model
we are using serializers.Serializer because we have limited operations
"""
from rest_framework import serializers
from django.utils import timezone


class ToDoListSerializer(serializers.Serializer):
    """
    all attributes will be read only because it will be useless to make it
    editable while we are going to edit only finished_at and is_finished
    dynamically when user request to change todo task status
    we will add create function without implementation because it's abstract method
    which is not important
    """

    id = serializers.IntegerField(read_only=True)
    creator_username = serializers.CharField(source="creator.username", read_only=True)
    description = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    finished_at = serializers.DateTimeField(read_only=True)
    is_finished = serializers.BooleanField(read_only=True)
    due_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.is_finished = True
        instance.finished_at = timezone.now()
        instance.save(update_fields=["is_finished", "finished_at"])
        return instance
