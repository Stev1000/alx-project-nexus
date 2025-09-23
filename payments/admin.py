from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "amount", "payment_status", "payment_method", "payment_date", "transaction_id")
    list_filter = ("payment_status", "payment_method", "payment_date")
    search_fields = ("order__id", "transaction_id")
    ordering = ("-payment_date",)
