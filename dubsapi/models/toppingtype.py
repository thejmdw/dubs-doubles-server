from django.db import models


class ToppingType(models.Model):

    name = models.CharField(max_length=55)