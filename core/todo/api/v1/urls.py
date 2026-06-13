from rest_framework.routers import DefaultRouter
from todo.api.v1.views import (
    TaskViewSet,
)

app_name = "api-v1"

router = DefaultRouter()
router.register("task", TaskViewSet, basename="task")
urlpatterns = router.urls

# app_name = 'api-v1'

# urlpatterns = [
#     path('task/', task_view, name='task-list'),
#     path('task/<int:id>', task_detail, name='task-detail'),
# ]
