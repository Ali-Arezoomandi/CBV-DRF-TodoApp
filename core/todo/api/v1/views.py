from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from todo.models import Task
from todo.api.v1.serializers import TaskSerializer
from todo.api.v1.permissions import CustomPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from todo.api.v1.paginations import DefaultPagination

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def task_view(request):
#     tasks = Task.objects.all()
#     if request.method == 'GET':
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def task_detail(request, id):
#     task = Task.objects.get(pk=id)
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response({'detail': 'deleted post was successfully'}, status=status.HTTP_204_NO_CONTENT)


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
