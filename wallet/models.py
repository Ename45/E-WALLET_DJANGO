import datetime
from uuid import uuid4

from django.conf import settings
from django.db import models


# Create your models here.


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    wallet_number = models.CharField(max_length=10, primary_key=True, unique=True)
    # date_created = models.DateTimeField(default=datetime.datetime.now())


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit')
    ]

    TRANSACTION_STATUS = [
        ('SUCCESSFUL', 'Successful'),
        ('PENDING', 'Pending'),
        ('DECLINED', 'Declined')
    ]
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE, default="Debit")
    transaction_status = models.CharField(max_length=10, choices=TRANSACTION_STATUS, default="Successful")
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='transactions')
    reference_number = models.UUIDField(primary_key=True, default=uuid4, editable=False)
