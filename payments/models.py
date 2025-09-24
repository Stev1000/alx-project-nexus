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

    order = models.OneToOneField(Order, related_name="payment", on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"
