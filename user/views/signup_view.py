from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers.signup import SignupSerializer, signup_schema
from drf_yasg.utils import swagger_auto_schema

class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny] 
    http_method_names = ['post']

    @swagger_auto_schema(
        request_body=signup_schema,
        responses={201: "Conta criada com sucesso!", 400: "Erro de validação"},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Conta criada com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
