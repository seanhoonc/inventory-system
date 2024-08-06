from django.db import models


class Supplier(models.Model):
    name = models.CharField(
        max_length=100,
    )
    address = models.CharField(
        max_length=150,
    )
    contact_name = models.CharField(
        max_length=50,
    )
    email = models.CharField(
        max_length=100,
    )
