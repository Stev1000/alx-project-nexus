from django.db import models
from users.models import User
from products.models import Product

class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # one review per user per product

    def __str__(self):
        return f"{self.user.username} review for {self.product.name}"
