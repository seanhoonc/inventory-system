from django.db import models
from common.models import CommonModel
from django.core.validators import MaxValueValidator


class Order(CommonModel):
    """Order Model Definition"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
    )

    item = models.ManyToManyField(
        "items.Item",
    )

    order_qty = models.PositiveIntegerField(
        validators=[MaxValueValidator(200)],
    )

    due = models.DateTimeField(
        verbose_name="Due By",
    )

    def __str__(self):
        return f"Order #{self.id}"
