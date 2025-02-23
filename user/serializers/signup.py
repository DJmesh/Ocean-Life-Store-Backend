from rest_framework import serializers
from user.models import MyUser
from drf_yasg import openapi

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = [
            "email",
            "full_name",
            "username",
            "date_of_birth",
            "password",
            "confirm_password",
        ]

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            username=validated_data["username"],
            date_of_birth=validated_data["date_of_birth"],
            password=validated_data["password"],
        )
        return user

# Definir um schema para o Swagger manualmente
signup_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário"),
        "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="Nome completo"),
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="Nome de usuário"),
        "date_of_birth": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description="Data de nascimento (YYYY-MM-DD)"),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description="Senha do usuário"),
        "confirm_password": openapi.Schema(type=openapi.TYPE_STRING, description="Confirmação de senha"),
    },
    required=["email", "full_name", "username", "date_of_birth", "password", "confirm_password"],
)
