from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Product


# Create your tests here.

class ProductTestCase(APITestCase):
    """
    Test suite for Product
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='simple_test_password',
            email='test@test.com'
        )
        # Set up token authentication
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        # Pass the token in all calls to the API
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.data = {
            "name": "Product 1",
            "image": "",
            "variants": [
                {
                    "sku": "SKU001",
                    "name": "Variant 1",
                    "price": 19.99,
                    "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "product_id": "1"
                },
            ]
        }
        self.url = "/products/"

    def test_create_product(self):
        """
        test ProductViewSet create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Product 1")

    def test_create_product_without_name(self):
        """
        test ProductViewSet create method when name is not in data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_without_variant(self):
        """
        test ProductViewSet create method when name is not in data
        """
        data = self.data
        data.pop("variants")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



