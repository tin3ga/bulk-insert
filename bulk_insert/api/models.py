from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/", null=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    details = models.CharField(max_length=100)
    product_id = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
