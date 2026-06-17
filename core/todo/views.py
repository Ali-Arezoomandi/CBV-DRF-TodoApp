from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from todo.models import Task
from todo.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    """
    a class for show all task
    """

    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    a class for create new task
    """

    model = Task
    form_class = TaskForm
    success_url = "/"
    template_name = "todo/task_form_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    a class for update a task
    """

    model = Task
    form_class = TaskForm
    success_url = "/"
    template_name = "todo/task_form_update.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    a class for delete a task
    """

    model = Task
    success_url = "/"
    context_object_name = "task"
    template_name = "todo/task_form_delete.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
