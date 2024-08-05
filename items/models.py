from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(
        verbose_name="Price",
    )
    urgent = models.BooleanField(
        default=False, verbose_name="urgent?", help_text="is it urgent?"
    )
    description = models.TextField()

    def __str__(self):
        return self.name
