from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db import IntegrityError  # ✅ added
from .models import Payment
from .serializers import PaymentSerializer

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:  # ✅ handle OneToOneField duplicate errors
            return Response(
                {"error": "This order already has a payment."},
                status=status.HTTP_400_BAD_REQUEST
            )

class PaymentHistoryView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # ✅ Only return current user’s payments
        return Payment.objects.filter(order__user=self.request.user).order_by("-payment_date")
