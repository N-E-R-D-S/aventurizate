from django.contrib import admin
from .models import Tour, TourReservation


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "guide",
        "date",
        "max_participants",
        "spots_taken",
        "spots_available",
        "published",
    )
    list_filter = ("published", "date", "guide")
    search_fields = ("name", "description", "guide__user__username")
    ordering = ("-date",)
    date_hierarchy = "date"


@admin.register(TourReservation)
class TourReservationAdmin(admin.ModelAdmin):
    list_display = (
        "tour",
        "tourist",
        "is_confirmed",
        "reserved_at",
    )
    list_filter = ("is_confirmed", "reserved_at", "tour")
    search_fields = (
        "tour__name",
        "tourist__user__username",
    )
    ordering = ("-reserved_at",)
