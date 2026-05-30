from django.shortcuts import render
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
    context_object_name = 'tasks'
    
    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks
    
    
class TaskCreateView(CreateView):
    """
    a class for create new task
    """
    model = Task
    form_class = TaskForm
    success_url = '/'
    template_name = 'todo/task_form_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskUpdateView(UpdateView):
    """
    a class for update a task
    """
    model = Task
    form_class = TaskForm
    success_url = '/'
    template_name = 'todo/task_form_update.html'
       

class TaskDeleteView(DeleteView):
    """
    a class for delete a task
    """
    context_object_name = 'task'
    model = Task
    success_url = '/'


 