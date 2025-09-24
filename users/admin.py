from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone", "role", "is_active", "is_staff", "is_admin", "date_joined")
    list_filter = ("role", "is_active", "is_staff", "is_admin", "date_joined")
    search_fields = ("username", "email", "phone")
    ordering = ("-date_joined",)
