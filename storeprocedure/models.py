from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(User):
    fields = ["username", "email", "password"]

class stock_inventory(models.Model):
    user = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True,null = True)
    product_title = models.CharField(max_length=25)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length= 100)
    @property
    def __str__(self):
        return self.product_title
