from rest_framework import serializers
from user.models.user import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo MyUser.
    """
    avatar = serializers.ImageField(required=False, allow_null=True)  
    email = serializers.EmailField(required=False)  
    full_name = serializers.CharField(required=False)  
    username = serializers.CharField(required=False)  
    date_of_birth = serializers.DateField(required=False, allow_null=True)  
    bio = serializers.CharField(required=False, allow_blank=True) 
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    confirm_password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    cover = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = MyUser
        fields = [
            "id",
            "email",
            "full_name",
            "username",
            "date_of_birth",
            "bio",
            "is_active",
            "is_staff",
            "is_superuser",
            "followers_count",
            "following_count",
            "publications_count",
            "favorite_publications_count",
            "avatar",
            "cover",
            "password",
            "confirm_password",
        ]

    def validate(self, data):
        """
        Valida se as senhas coincidem apenas quando ambas forem fornecidas.
        """
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})

        data.pop("confirm_password", None)  # Remove confirm_password após validação
        return data

    def update(self, instance, validated_data):
        """
        Atualiza os dados do usuário, incluindo a senha se fornecida.
        """
        password = validated_data.pop("password", None)  # Remove e armazena a senha, se fornecida

        # Atualiza os campos enviados
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Atualiza a senha, se fornecida
        if password:
            instance.set_password(password)

        instance.save()
        return instance
