from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationApiSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password1"]

    def validate(self, attrs):
        # check that passwords is same
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "passwords does not match"}
            )

        # check complexity of password after matching
        try:
            validate_password(attrs.get("password"))
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.message)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["user_id"] = self.user.pk
        validated_data["username"] = self.user.username
        return validated_data


class ChangePasswordApiSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        max_length=255, required=True, write_only=True
    )
    new_password = serializers.CharField(
        max_length=255, required=True, write_only=True
    )
    new_password1 = serializers.CharField(
        max_length=255, required=True, write_only=True
    )

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError(
                {"detail": "passwords does not match"}
            )
        try:
            validate_password(attrs.get("new_password"))
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.message)})

        return super().validate(attrs)


class ActivationResendApiSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "user does not exist"}
            )
        if user.is_verified:
            raise serializers.ValidationError(
                {"detail": "user is already activated and verified"}
            )
        attrs["user"] = user
        return super().validate(attrs)
