from django.db import models


class ProductType(models.Model):

    name = models.CharField(max_length=55)