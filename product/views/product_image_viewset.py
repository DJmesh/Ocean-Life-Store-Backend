from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from product.models import ProductImage
from product.serializers.product_serializer import ProductImageSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento das imagens dos produtos.
    Permite listar, criar, atualizar e excluir imagens.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny] 
