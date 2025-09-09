from django.urls import path
from . import views

app_name = "birds"

urlpatterns = [
    path("", views.bird_list, name="bird_list"),
    path("<slug:slug>/", views.bird_detail, name="bird_detail"),
]
