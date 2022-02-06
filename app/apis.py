"""
Api file which will represent all apis for todo from mobile devices
"""
from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Todo
from .serilaizers import ToDoListSerializer


class ToDoListApi(
    GenericViewSet, ListAPIView, UpdateAPIView
):  # pylint: disable=too-many-ancestors
    """
    api will do listing and updating end-user todo list
    listing (GET): will show all list which can be filtered by is_finished and due_date
    api ex: GET => host:port/api/mobile/v1/todo/?is_finished=true
    update (PATCH/PUT): will handle updating status (is_finished)
    api ex : PATCH/PUT => host:port/api/mobile/v1/todo/ with {} as body
    """

    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = ToDoListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_finished", "due_date"]

    def get_object(self):
        return get_object_or_404(Todo, id=self.kwargs.get("pk"), is_finished=False)

    def get_queryset(self) -> QuerySet:
        return Todo.objects.filter(end_user=self.request.user).order_by("-id")
