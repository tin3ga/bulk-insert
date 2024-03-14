from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import ProductVariant,Product
from .serializers import ProductVariantSerializer, ProductSerializer


# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductVariantListCreate(generics.ListCreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer