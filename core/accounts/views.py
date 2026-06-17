from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from accounts.forms import CustomUSerCreationFrom
from django.urls import reverse_lazy


# Create your views here.
class UserLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task-list")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUSerCreationFrom

    def get_success_url(self):
        return reverse_lazy("accounts:login")
