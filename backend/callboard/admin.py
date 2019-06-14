from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Advert, FilterAdvert, DateAdvert
# Register your models here.

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    list_display = ("name", "id")
    mptt_level_indent = 20
    prepopulated_fields = {"slug": ("name",)}

@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    """Фильтры"""
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(DateAdvert)
class DateAdvertAdmin(admin.ModelAdmin):
    """Срок для объявления"""
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        "user",
        "category",
        "filters",
        "date",
        "price",
        "create",
        "moderation"
    )
    list_display_links = ("subject",)
    list_filter = ("user", "category", "filters", "date", "price")
    prepopulated_fields = {"slug": ("user", "subject")}
