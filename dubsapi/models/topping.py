from django.db import models
from .toppingtype import ToppingType

class Topping(models.Model):

    name = models.CharField(max_length=50,)
    price = models.FloatField()
    topping_type = models.ForeignKey(
        ToppingType, on_delete=models.DO_NOTHING, related_name='products')