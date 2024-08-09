from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Details",
            {
                "fields": (
                    "item_photo",
                    "name",
                    (
                        "price",
                        "currency",
                    ),
                    "qty",
                    "category",
                    "suppliers",
                    "description",
                    "urgent",
                )
            },
        ),
    )
    list_display = (
        "name",
        "price",
        "currency",
        "category",
    )
    list_filter = ("name", "price", "currency")
    search_fields = ("name", "category")
