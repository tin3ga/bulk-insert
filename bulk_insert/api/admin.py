from django.contrib import admin

from . models import Product, ProductVariant

# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(ProductVariant)
class ProductVariant(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'price', 'details', 'product_id')