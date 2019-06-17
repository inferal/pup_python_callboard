from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """Модель профиля пользователя"""
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="profile/")
    email_two = models.EmailField("Доп. email")