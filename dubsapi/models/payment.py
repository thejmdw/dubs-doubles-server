from django.db import models
from .customer import Customer
# from safedelete.models import SafeDeleteModel
# from safedelete.models import SOFT_DELETE

# class Payment(SafeDeleteModel):
class Payment(models.Model):
    # _safedelete_policy = SOFT_DELETE
    merchant_name = models.CharField(max_length=25)
    account_number = models.IntegerField()
    expiration_date = models.CharField(max_length=7)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name="payment_types")
    created_on = create_date = models.DateField(default="0000-00-00",)    