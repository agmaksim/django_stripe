from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=100
    )
    stripe_product_id = models.CharField(
        max_length=100
        )
    description = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(
        max_length=100
    )
    price = models.IntegerField(
        default=0
        )

    def get_display_price(self):
        return "{0:.2f}".format(self.price)

