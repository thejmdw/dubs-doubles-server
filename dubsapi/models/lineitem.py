from dubsapi.models.lineitemtopping import LineItemTopping
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

    @property
    def liToppings(self):
        toppingsList = LineItemTopping.objects.filter(line_item=self)

        return toppingsList