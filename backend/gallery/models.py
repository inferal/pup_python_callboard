from django.db import models

# Create your models here.

class Gallery(models.Model):
    """Галерея"""
    name = models.CharField("Имя" , max_length=50)
    photos = models.ManyToManyField(verbose_name="Фотографии")
    slug = models.SlugField("url", max_length=50, unique=True)
