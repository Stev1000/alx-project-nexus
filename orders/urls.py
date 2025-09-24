from django.urls import path
from .views import PlaceOrderView, UserOrdersView, OrderDetailView

urlpatterns = [
    path("place/", PlaceOrderView.as_view(), name="place-order"),
    path("my-orders/", UserOrdersView.as_view(), name="user-orders"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
