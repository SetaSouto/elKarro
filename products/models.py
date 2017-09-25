from django.db import models


class Product(models.Model):
    """
    Product
    """
    number = models.IntegerField()
    # Optional name and description for the product
    name = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=500)


class Order(models.Model):
    """
    Order that has a name (the buyer), a creation datetime, a state (delivered or not) and products.
    """
    creation_datetime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    delivered = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)
