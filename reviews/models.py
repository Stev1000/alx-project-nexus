from django.db import models
from users.models import User
from products.models import Product

class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE, db_index=True)
    rating = models.IntegerField(db_index=True)
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ('user', 'product')
        indexes = [
            models.Index(fields=['rating']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.user.username} review for {self.product.name}"
