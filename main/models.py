from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    Category = models.TextField()
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()