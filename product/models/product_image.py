import os
from django.db import models
from .product import Product

def product_image_upload_path(instance, filename):
    """
    Retorna o caminho de upload: produtos/<guid_do_produto>/<nome_do_produto>/<nome_arquivo>
    """
    return os.path.join(
        "produtos",
        str(instance.product.guid),
        instance.product.name,
        filename
    )

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=product_image_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem de {self.product.name}"
