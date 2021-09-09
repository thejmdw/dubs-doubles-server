from django.db import models

class LineItemTopping(models.Model):
    topping = models.ForeignKey("Topping", on_delete=models.CASCADE)
    line_item = models.ForeignKey("LineItem", on_delete=models.CASCADE)