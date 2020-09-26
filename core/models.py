from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price}"