from django.db import models


class LineItem(models.Model):

    order = models.ForeignKey("Order",
                              on_delete=models.DO_NOTHING,
                              related_name="lineitems")

    product = models.ForeignKey("Product",
                                on_delete=models.DO_NOTHING,
                                related_name="lineitems")
    
    toppings = models.ManyToManyField("Topping",
                                through="LineItemTopping",
                                related_name="lineitemtoppings")
