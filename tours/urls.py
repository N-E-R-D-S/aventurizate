from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.list_tours, name="tour_list"),
    path("create/", views.create_tour, name="create_tour"),
    path("my-tours/", views.my_tours, name="my_tours"),
    path("<int:tour_id>/", views.tour_detail, name="tour_detail"),
    path("<int:tour_id>/reserve/", views.reserve_tour, name="reserve_tour"),
    path("my-reservations/", views.my_reservations, name="my_reservations"),
    path("<int:tour_id>/participants/",
         views.tour_participants, name="tour_participants"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/<int:reservation_id>/', views.payment_view, name='payment'),
    path('payment/done/', views.payment_done, name='payment_done'),
    path('payment/cancelled/', views.payment_cancelled, name='payment_cancelled'),
]
