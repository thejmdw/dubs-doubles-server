from django.db import models
from .customer import Customer

class Payment(models.Model):
    
    merchant_name = models.CharField(max_length=25)
    account_number = models.IntegerField()
    expiration_date = models.CharField(max_length=7)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name="payment_types")
    created_on = models.DateField(auto_now_add=True)    