from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListCreate.as_view(), name="product-view-create"),
    path("product_variant/", views.ProductVariantListCreate.as_view(), name="product-variant-view-create"),
]