from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE, db_index=True)
    order_date = models.DateTimeField(auto_now_add=True, db_index=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', db_index=True)
    shipping_address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['total_price']),
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE, db_index=True)
    quantity = models.PositiveIntegerField(default=1, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
