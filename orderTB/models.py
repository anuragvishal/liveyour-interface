from django.db import models



class Orders(models.Model):
    order_id = models.CharField(max_length=255, blank=True)
    product_name = models.CharField(max_length=255, blank=True)
    order_status = models.CharField(max_length=100, blank=True)
    product_url = models.CharField(max_length=255, blank=True)
    cost_price = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'orders'
