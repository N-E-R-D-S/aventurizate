from django.contrib import admin
from .models import (
    BirdType, Habitat, BirdOrder, BirdFamily, BirdGenus,
    BirdSpecies, BirdPhoto, BirdObservation, BirdDistributionMap
)


@admin.register(BirdType)
class BirdTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(BirdOrder)
class BirdOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(BirdFamily)
class BirdFamilyAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "description")
    list_filter = ("order",)
    search_fields = ("name", "order__name")


@admin.register(BirdGenus)
class BirdGenusAdmin(admin.ModelAdmin):
    list_display = ("name", "family", "description")
    list_filter = ("family",)
    search_fields = ("name", "family__name")


@admin.register(BirdSpecies)
class BirdSpeciesAdmin(admin.ModelAdmin):
    list_display = ("common_name", "scientific_name", "genus", "bird_type")
    list_filter = ("genus", "bird_type", "habitats")
    search_fields = ("common_name", "scientific_name")
    filter_horizontal = ("habitats",)  # Para ManyToMany


@admin.register(BirdPhoto)
class BirdPhotoAdmin(admin.ModelAdmin):
    list_display = ("bird", "description", "created_at")
    list_filter = ("bird",)
    search_fields = ("bird__common_name", "description")


@admin.register(BirdObservation)
class BirdObservationAdmin(admin.ModelAdmin):
    list_display = ("bird", "observer", "date_observed", "count")
    list_filter = ("bird", "observer", "date_observed")
    search_fields = ("bird__common_name", "observer__username", "note")
    filter_horizontal = ("photos",)


@admin.register(BirdDistributionMap)
class BirdDistributionMapAdmin(admin.ModelAdmin):
    list_display = ("bird", "description", "created_at")
    list_filter = ("bird",)
    search_fields = ("bird__common_name", "description")
