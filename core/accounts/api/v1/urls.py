from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView, 
    TokenVerifyView
)

urlpatterns = [
    # registration
    path('registration/', RegistrationApiView.as_view(), name='registration'),

    # activation/resend activation
    path('activation/confirm/<str:token>', ActivationApiView.as_view(), name='activation'),
    path('activation/resend/', ActivationResendApiView.as_view(), name='activation-resend'),
    
    # change/reset password
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),

    # login/logout token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    # create/refresh/verify jwt
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refrsh/', TokenRefreshView.as_view(), name='jwt-refrsh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]