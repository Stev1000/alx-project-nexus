# products/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - SAFE_METHODS (GET, HEAD, OPTIONS) → allowed for everyone
    - Other methods (POST, PUT, DELETE) → only allowed for admin users
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
 # Filtering, sorting, searching
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']  # filter by category or price
    search_fields = ['name', 'description']  # search by name or description
    ordering_fields = ['price', 'created_at', 'updated_at']  # allow ordering by these
    ordering = ['-created_at']  # default order (latest first)