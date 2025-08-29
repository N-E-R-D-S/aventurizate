from django.contrib import admin
from .models import (
    Type, Habitat, Order, Family, Genus,
    Species, Photo, Observation, DistributionMap
)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "description")
    list_filter = ("order",)
    search_fields = ("name", "order__name")


@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ("name", "family", "description")
    list_filter = ("family",)
    search_fields = ("name", "family__name")


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("common_name", "scientific_name", "genus", "type")
    list_filter = ("genus", "type", "habitats")
    search_fields = ("common_name", "scientific_name")
    filter_horizontal = ("habitats",)  # Para ManyToMany


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("bird", "description", "created_at")
    list_filter = ("bird",)
    search_fields = ("bird__common_name", "description")


@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ("bird", "observer", "date_observed", "count")
    list_filter = ("bird", "observer", "date_observed")
    search_fields = ("bird__common_name", "observer__username", "note")
    filter_horizontal = ("photos",)


@admin.register(DistributionMap)
class DistributionMapAdmin(admin.ModelAdmin):
    list_display = ("bird", "description", "created_at")
    list_filter = ("bird",)
    search_fields = ("bird__common_name", "description")
