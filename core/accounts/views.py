from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('todo:task-list')   
    

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse_lazy('accounts:login')
    
    