from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Language, Country, TouristProfile, GuideProfile


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "alpha_2", "alpha_3")
    search_fields = ("name", "alpha_2", "alpha_3")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "alpha_2", "alpha_3", "official_name")
    search_fields = ("name", "alpha_2", "alpha_3", "official_name")


# Perfil de turistas
@admin.register(TouristProfile)
class TouristProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "country")
    search_fields = ("user__username", "country__name")
    autocomplete_fields = ("user", "country")


# Perfil de guías
@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "experience_years")
    search_fields = ("user__username", "phone_number")
    autocomplete_fields = ("user",)


# Usuario personalizado
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": (
            "first_name", "last_name", "email", "picture", "bio", "languages")}),
        ("Permissions", {"fields": ("is_active", "is_staff",
         "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = ("groups", "user_permissions", "languages")
