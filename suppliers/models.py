from django.db import models
from common.models import CommonModel


class Supplier(CommonModel):
    name = models.CharField(
        max_length=100,
        default="",
    )
    address = models.CharField(
        max_length=150,
        default="",
    )
    contact_name = models.CharField(
        max_length=50,
    )
    email = models.CharField(
        max_length=100,
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
