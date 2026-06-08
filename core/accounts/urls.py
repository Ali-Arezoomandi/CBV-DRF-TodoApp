from django.urls import path, include
from accounts.views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/v1/', include('accounts.api.v1.urls')),
    # path('api/v2/', include('djoser.urls')),
    # path('api/v2/', include('djoser.urls.jwt')),
]

