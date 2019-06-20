from django.contrib import admin

# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ("user", "email_two", "first_name")