from rest_framework import serializers
from product.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'uploaded_at')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'guid', 'name', 'description', 'price', 'created_at', 'updated_at', 'images')
