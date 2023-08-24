from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin panel"""
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_active']
    list_display_links = list_display
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    search_fields = ['id', 'first_name', 'last_name', 'email']
    fields = ['email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']
