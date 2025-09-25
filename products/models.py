from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['name'])]


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    stock_quantity = models.PositiveIntegerField(default=0, db_index=True)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
            models.Index(fields=['created_at']),
        ]
