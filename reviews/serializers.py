# reviews/serializers.py
from rest_framework import serializers
from .models import Review
from products.serializers import ProductSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username
    product = ProductSerializer(read_only=True)            # nested product info
    product_id = serializers.IntegerField(write_only=True) # used when creating

    class Meta:
        model = Review
        fields = ["id", "user", "product", "product_id", "rating", "review_text", "created_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
