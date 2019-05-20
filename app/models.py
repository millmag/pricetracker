"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.cname


class Product(models.Model):
    pname = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    unit = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname


class Shop(models.Model):
    sname = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.sname


class PriceTracker(models.Model):
    date = models.DateField()
    pname = models.ForeignKey(Product, on_delete=models.CASCADE)
    sname = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)

