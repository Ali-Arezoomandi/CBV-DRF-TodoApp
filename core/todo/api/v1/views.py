from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import ModelViewSet
from todo.models import Task
from todo.api.v1.serializers import TaskSerializer
from todo.api.v1.permissions import CustomPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from todo.api.v1.paginations import DefaultPagination


class TaskViewSet(ModelViewSet):
    """
    a class from ModelViewSet for show all tasks and single task
    """

    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["completed"]
    search_fields = ["title"]
    ordering_fields = ["created_date"]
    pagination_class = DefaultPagination
