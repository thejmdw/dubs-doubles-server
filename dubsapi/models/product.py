from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# from safedelete.models import SafeDeleteModel
# from safedelete.models import SOFT_DELETE
from .customer import Customer
from .producttype import ProductType


# class Product(SafeDeleteModel):
class Product(models.Model):

    # _safedelete_policy = SOFT_DELETE
    name = models.CharField(max_length=50,)
    price = models.FloatField()
    description = models.CharField(max_length=255,)
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    product_type = models.ForeignKey(
        ProductType, on_delete=models.DO_NOTHING, related_name='products')
    image_path = models.ImageField(
        upload_to='products', height_field=None,
        width_field=None, max_length=None, null=True)