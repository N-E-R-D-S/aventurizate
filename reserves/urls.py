from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserve_list, name='reserve_list'),
    path('<int:pk>/', views.reserve_detail,
         name='reserve_detail'),
]
