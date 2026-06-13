from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from .serializers import (
    RegistrationApiSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordApiSerializer,
    ActivationResendApiSerializer,
)
from django.core.mail import send_mail
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings


# for accounts/api/v1/registration
class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationApiSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_obj = serializer.save()

            data = {"username": serializer.validated_data["username"]}

            email = serializer.validated_data["email"]
            token = self.get_token_for_user(user_obj)
            send_mail(
                "Activation Email",
                f"http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{token}",
                "admin@admin.com",
                [f"{email}"],
            )

            print("==================")
            print("token:", token)
            print("==================")

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_token_for_user(self, user_obj):
        refresh = RefreshToken.for_user(user_obj)
        return str(refresh.access_token)


# for accounts/api/v1/token/login
class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serialzier = self.get_serializer(
            data=request.data, context={"reauest": request}
        )
        serialzier.is_valid(raise_exception=True)
        user = serialzier.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
            }
        )


# for accounts/api/v1/token/logout
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# for accounts/api/v1/jwt/create
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# for accounts/api/v1/change-password
class ChangePasswordApiView(GenericAPIView):
    serializer_class = ChangePasswordApiSerializer

    def get_object(self):
        user_obj = self.request.user
        return user_obj

    def put(self, request, *args, **kwargs):
        user_obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user_obj.check_password(serializer.validated_data["old_password"]):
                return Response(
                    {"old_password": ["Wrong password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user_obj.set_password(serializer.validated_data["new_password"])
            user_obj.save()

            return Response(
                {"detail": "password change successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for accounts/api/v1/activation/confirm/<str:token>
class ActivationApiView(GenericAPIView):

    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response(
                {"detail": "token has beem expire"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidSignatureError:
            return Response(
                {"detail": "token is not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.get(pk=user_id)
        if user.is_verified:
            return Response({"detail": "your account have already been verified."})
        user.is_verified = True
        user.save()

        return Response(
            {"detail": "your account have been verified and activated successfully."}
        )


class ActivationResendApiView(GenericAPIView):
    serializer_class = ActivationResendApiSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_token_for_user(user_obj)
        send_mail(
            "Activation Resend Email",
            f"http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{token}",
            "admin@admin.com",
            [f"{serializer.validated_data['email']}"],
        )

        print("==================")
        print("token:", token)
        print("==================")

        return Response(
            {"detail": "user activation resend successfully"},
            status=status.HTTP_200_OK,
        )

    def get_token_for_user(self, user_obj):
        refresh = RefreshToken.for_user(user_obj)
        return str(refresh.access_token)
