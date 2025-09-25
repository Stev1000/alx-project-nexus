"""
URL configuration for ecommerce_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from products.views import CategoryViewSet, ProductViewSet
from carts.views import CartView, AddToCartView, UpdateCartItemView, RemoveCartItemView
from orders.views import PlaceOrderView, UserOrdersView, OrderDetailView
from reviews.views import ReviewViewSet
from django.conf import settings
from django.conf.urls.static import static
# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")
router.register("reviews", ReviewViewSet, basename="review")

# Swagger schema
schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version="v1",
        description="API documentation for Project Nexus E-Commerce Backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@nexus.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    return HttpResponse("Welcome to Project Nexus E-Commerce API")

urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # JWT auth endpoints
    path("api/", include(router.urls)),  # Products & Categories
    path("api/payments/", include("payments.urls")),

    # Cart Endpoints (do not interfere with router ones)
    path("api/cart/", CartView.as_view(), name="cart-detail"),
    path("api/cart/add/", AddToCartView.as_view(), name="cart-add"),
    path("api/cart/update/<int:pk>/", UpdateCartItemView.as_view(), name="cart-update"),
    path("api/cart/remove/<int:pk>/", RemoveCartItemView.as_view(), name="cart-remove"),

    # Order endpoints
    path("api/orders/", include("orders.urls")),
    path("api/orders/place/", PlaceOrderView.as_view(), name="order-place"),
    path("api/orders/", UserOrdersView.as_view(), name="user-orders"),
    path("api/orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),

    # Swagger / ReDoc
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)