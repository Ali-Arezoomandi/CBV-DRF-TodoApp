from django.urls import path, include
from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="create-task"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"),
    path("api/v1/", include("todo.api.v1.urls")),
]
