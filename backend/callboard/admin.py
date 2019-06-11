from django.contrib import admin

from .models import Category, Advert, FilterAdvert, DateAdvert
# Register your models here.

admin.site.register(Category)
admin.site.register(Advert)
admin.site.register(FilterAdvert)
admin.site.register(DateAdvert)
