from django.urls import path
from .views import PaymentCreateView, PaymentHistoryView

urlpatterns = [
    path("pay/", PaymentCreateView.as_view(), name="make_payment"),
    path("history/", PaymentHistoryView.as_view(), name="payment_history"),
]
