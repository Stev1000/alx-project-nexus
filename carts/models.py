from django.db import models
from users.models import User
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart ({self.user.username})"

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, related_name="cart_items", on_delete=models.CASCADE, db_index=True)
    quantity = models.PositiveIntegerField(default=1, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('cart', 'product')
        indexes = [
            models.Index(fields=['quantity']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
