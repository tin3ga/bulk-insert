from rest_framework import serializers
from .models import ProductVariant, Product


class ProductBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        product_list = []
        for item in validated_data:
            product_list.append(Product(name=item['name'], image=item['image']))
        products = Product.objects.bulk_create(product_list)
        return products


class VariantBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        variant_list = []
        for item in validated_data:
            variant_list.append(
                ProductVariant(sku=item['sku'], name=item['name'], price=item['price'], details=item['details'],
                               product_id=item['product_id']))
        product_variants = ProductVariant.objects.bulk_create(variant_list)
        return product_variants


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'
        list_serializer_class = VariantBulkCreateSerializer


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "image", 'variants']
        list_serializer_class = ProductBulkCreateSerializer
