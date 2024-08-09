from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """Item or Supplier Category"""

    class CategoryKindChoices(models.TextChoices):
        ITEMS = "items", "Items"
        SUPPLIERS = "suppliers", "Suppliers"

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
