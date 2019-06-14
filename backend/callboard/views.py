from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Advert


class AdvertList(ListView):
    """Все объявления"""

    model = Advert
    queryset = Advert.objects.all()
    template_name = "callboard/advert-list.html"

class AdvertDetail(DetailView):
    """Подробно об оъбявлении"""
    model = Advert
    context_object_name = "advert"
    template_name = "callboard/advert-detail.html"