from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=128, null=True, blank=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    company_vat = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    zip_code = models.CharField(max_length=128, null=True, blank=True)


class Seller(models.Model):
    FORTNOX = 'fortnox'
    VISMA = 'visma'
    ACCOUNT_TYPES = [
        (FORTNOX, 'Fortnox'),
        (VISMA, 'Visma'),
    ]
    customer_no = models.CharField(max_length=128)
    customer_name = models.CharField(max_length=128)
    account_type = models.CharField(max_length=128, choices=ACCOUNT_TYPES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellers')
