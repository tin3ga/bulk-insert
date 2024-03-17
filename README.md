# bulk-insert

A Django API designed to handle the insertion of products and their variants, utilizing Django REST Framework. It
supports both single and bulk data insertion operations.


![GitHub top language](https://img.shields.io/github/languages/top/tin3ga/bulk-insert)
![GitHub License](https://img.shields.io/github/license/tin3ga/bulk-insert)
![GitHub last commit](https://img.shields.io/github/last-commit/tin3ga/bulk-insert)

## Technologies

- [Django](https://www.djangoproject.com/)
- [djangorestframework](https://www.django-rest-framework.org/)
- ...

## Quick Start

1. Clone the repo:

```
$ git clone https://github.com/tin3ga/bulk-insert.git
$ cd bulk-insert
```

2. Initialize and activate a virtualenv:

```
# windows
$ python -m venv venv
$ venv\Scripts\activate

# mac/linux
$ python -m venv venv
$ source env/bin/activate or . venv/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

4. Navigate to bulk_insert:

```
$ cd bulk_insert
```

5. Make Migrations:

```
$ python manage.py makemigrations
$ python manage.py migrate

```

6. Create SuperUser:


An auth token is automatically generated for new users and is to be contained in request headers when making api calls. Make sure to note your superuser name and password.


```
$ python manage.py createsuperuser

```

7. Run tests:

```
$ python manage.py test

```

8. Run the development server:

```
$ python manage.py runserver
```

## Endpoints

1. Retrieve Auth Token

```
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'content-type: multipart/form-data' \
  --form username=**your username** \
  --form password=**your password**
  
```

2. Bulk Insert Products

```
curl --request POST \
  --url http://127.0.0.1:8000/products/ \
  --header 'AUTHORIZATION: Token **your token**' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '[
	{
		"name": "Yoghurt",
		"image": null,
		"variants": []
	},
	{
		"name": "Milk",
		"image": null,
		"variants": []
	},
	{
		"name": "Juice",
		"image": null,
		"variants": []
	}
]'

```

3. Bulk Insert Product Variants

```
curl --request POST \
  --url http://127.0.0.1:8000/product_variants/ \
  --header 'AUTHORIZATION: Token **your token**' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.0' \
  --data '[
  {
    "sku": "SKU001",
    "name": "Variant 1",
    "price": 19.99,
    "details": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "product_id": "3"
  },
  {
    "sku": "SKU002",
    "name": "Variant 2",
    "price": 29.99,
    "details": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "product_id": "1"
  },
  {
    "sku": "SKU003",
    "name": "Variant 3",
    "price": 39.99,
    "details": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
    "product_id": "1"
  }
]'
```
