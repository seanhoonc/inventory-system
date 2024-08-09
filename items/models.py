from django.db import models
from common.models import CommonModel


class Item(CommonModel):
    """Item Model Definition"""

    class CurrencyChoices(models.TextChoices):
        NZD = "nzd", "New Zealand Dollar"
        USD = "usd", "US Dollar"

    item_photo = models.ImageField(
        default="",
        verbose_name="Product Photo",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(
        "Quantity",
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Price",
    )
    urgent = models.BooleanField(
        default=False,
        verbose_name="Urgent?",
        help_text="is it urgent?",
    )
    description = models.TextField()
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices,
        default="nzd",
    )
    suppliers = models.ManyToManyField(
        "suppliers.Supplier",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name
