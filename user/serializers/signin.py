from rest_framework import serializers
from django.contrib.auth import authenticate
from drf_yasg import openapi

class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciais inválidas.")

# Definir um schema para o Swagger manualmente
signin_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário"),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description="Senha do usuário"),
    },
    required=["email", "password"],
)
