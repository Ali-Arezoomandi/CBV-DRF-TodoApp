from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from todo.models import Task
from todo.api.v1.serializers import TaskSerializer
from todo.api.v1.permissions import CustomPermission


class TaskViewSet(ModelViewSet):
    """
    a class from ModelViewSet for show all tasks and single task
    """

    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["completed"]
    search_fields = ["title"]
    ordering_fields = ["created_date"]
    # pagination_class = DefaultPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@api_view(["GET"])
def clear_all_tasks(request):
    Task.objects.filter(user=request.user).delete()
    return Response({"detail": "deleted was successfully"})
