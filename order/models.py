from django.db import models
from django.contrib.auth import get_user_model

from products.models import *

User = get_user_model()

STATUSES = {
    ('D', 'Delivered'),
    ('ND', 'Not Delivered')
}

PAYMENT_METHODS = {
    ('card', 'CARD'),
    ('cash', 'CASH')
}

class Order(models.Model):
    product = models.ManyToManyField(Product, through='OrderItem')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, choices=STATUSES)
    payment = models.CharField(max_length=5, choices=PAYMENT_METHODS)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

