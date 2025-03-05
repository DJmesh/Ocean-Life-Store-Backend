from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento dos produtos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny] 