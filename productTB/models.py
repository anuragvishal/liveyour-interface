from django.db import models



class Products(models.Model):
    product_name = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'products'
