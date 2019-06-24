from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import Profile


class ProflieDetail(DetailView):
    """Профиль пользователя"""
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/user-detail.html"

    # def get_queryset(self):
    #     return Profile.objects.get(user__username=self.kwargs.get("slug"))