from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.api.v1.views import (
    TaskViewSet,
    clear_all_tasks,
)

app_name = "api-v1"

router = DefaultRouter()
router.register("task", TaskViewSet, basename="task")
# urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("clear-all", clear_all_tasks, name="clear-all"),
]
