# reviews/views.py
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from .models import Review
from .serializers import ReviewSerializer
from orders.models import OrderItem

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # users can see only their reviews
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        product_id = self.request.data.get("product_id")

        # Ensure the user has purchased this product before reviewing
        purchased = OrderItem.objects.filter(order__user=user, product_id=product_id).exists()
        if not purchased:
            raise ValidationError("You can only review products you have purchased.")

        serializer.save(user=user)
