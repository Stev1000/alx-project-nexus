from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock_quantity", "category", "created_at", "updated_at")
    list_filter = ("category", "created_at")
    search_fields = ("name", "description")
    ordering = ("-created_at",)
