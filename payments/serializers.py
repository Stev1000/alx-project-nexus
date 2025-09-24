from rest_framework import serializers
from .models import Payment
from orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Payment
        fields = ["id", "order_id", "payment_date", "payment_method", "amount", "payment_status"]
        read_only_fields = ["id", "payment_date", "payment_status"]

    def validate(self, data):
        request = self.context.get("request")  # ✅ added: get current user
        try:
            order = Order.objects.get(id=data["order_id"])
        except Order.DoesNotExist:
            raise serializers.ValidationError({"order_id": "Invalid order ID"})

        # ✅ Ensure order belongs to current user
        if order.user != request.user:
            raise serializers.ValidationError({"order_id": "This order does not belong to you"})

        # ✅ Prevent duplicate payments
        if hasattr(order, "payment"):
            raise serializers.ValidationError({"order_id": "This order is already paid"})

        # ✅ Ensure amount matches order total
        if float(data["amount"]) != float(order.total_price):
            raise serializers.ValidationError({"amount": "Amount must match the order total price"})

        return data

    def create(self, validated_data):
        order = Order.objects.get(id=validated_data["order_id"])

        payment = Payment.objects.create(
            order=order,
            payment_method=validated_data["payment_method"],
            amount=validated_data["amount"],
            payment_status="completed"  # 🔄 changed: auto mark as completed
        )

        # ✅ Mark the order as paid
        order.status = "paid"  # 🔄 changed: previously `payment_status`, must be `status`
        order.save()

        return payment
