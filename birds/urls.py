from django.urls import path
from . import views

urlpatterns = [
    path("", views.bird_list_view, name="bird_list"),
    path("<slug:slug>/", views.bird_detail_view, name="bird_detail"),
]
