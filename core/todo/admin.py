from django.contrib import admin
from todo.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "completed", "updated_date"]
    list_filter = ("completed",)


admin.site.register(Task, TaskAdmin)
