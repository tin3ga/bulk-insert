from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'product_variants', views.ProductVariantViewSet)

urlpatterns = router.urls
