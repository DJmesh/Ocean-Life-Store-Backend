from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from user.models import MyUser
from user.serializers.user_serializer import MyUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    /api/users/<username>/        → retrieve / patch pelo username
    /api/users/me/                → perfil do usuário autenticado
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch"]

    # --------- rotas padrão (username) ----------
    def retrieve(self, request, username=None):
        user = get_object_or_404(MyUser, username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, username=None):
        user = get_object_or_404(MyUser, username=username)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Perfil atualizado com sucesso!"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # --------- NOVO endpoint /me/ ----------
    @action(detail=False, methods=["get", "patch"], url_path="me")
    def me(self, request):
        """
        GET  /api/users/me/       → dados do usuário autenticado
        PATCH /api/users/me/      → atualização parcial do próprio perfil
        """
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # PATCH
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Perfil atualizado com sucesso!"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
