from django.urls import path

from .views import *

urlpatterns = [
    path("", AdvertList.as_view(), name="advert_list"),
    path("<slug:category>/<slug:slug>/", AdvertDetail.as_view(), name="advert_detail")
]