from django.db import models
from orders.models import Order

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('card', 'Card'),
        ('mobile_money', 'Mobile Money'),
        ('paypal', 'PayPal'),
    )
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    order = models.OneToOneField(Order, related_name="payment", on_delete=models.CASCADE, db_index=True)
    payment_date = models.DateTimeField(auto_now_add=True, db_index=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, db_index=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending', db_index=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True, db_index=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"

    class Meta:
        indexes = [
            models.Index(fields=['payment_status']),
            models.Index(fields=['payment_date']),
        ]
