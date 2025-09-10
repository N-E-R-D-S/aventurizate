from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_tour, name="create_tour"),
    path("", views.list_tours, name="tour_list"),
    path("<int:tour_id>/", views.tour_detail, name="tour_detail"),
    path("<int:tour_id>/reserve/", views.reserve_tour, name="reserve_tour"),
    path("my-reservations/", views.my_reservations, name="my_reservations"),
    path("<int:tour_id>/participants/",
         views.tour_participants, name="tour_participants"),
]
