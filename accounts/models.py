from django.db import models
from django.contrib.auth.models import AbstractUser


class Language(models.Model):
    """Representa un idioma disponible en la plataforma."""
    name = models.CharField(max_length=100, unique=True)
    alpha_2 = models.CharField(
        max_length=2, unique=True, blank=True, null=True)
    alpha_3 = models.CharField(
        max_length=3, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.alpha_2 or self.alpha_3})"


class Country(models.Model):
    """Representa un país disponible en la plataforma."""
    name = models.CharField(max_length=100, unique=True)
    alpha_2 = models.CharField(max_length=2, unique=True)
    alpha_3 = models.CharField(max_length=3, unique=True)
    official_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name} ({self.alpha_2})"


class User(AbstractUser):
    """Usuario personalizado que extiende el modelo base de Django."""
    picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True)
    bio = models.TextField(blank=True)

    def get_group(self):
        """Obtiene el nombre del primer grupo al que pertenece el usuario."""
        return self.groups.first().name if self.groups.exists() else None

    def is_tourist(self):
        """Indica si el usuario pertenece al grupo 'Tourist'."""
        return self.get_group() == "Tourist"

    def is_guide(self):
        return self.get_group() == "Guide"

    def has_profile(self):
        """Verifica si el usuario ya tiene un perfil asociado según su grupo."""
        if self.is_tourist():
            return hasattr(self, "touristprofile")
        elif self.is_guide():
            return hasattr(self, "guideprofile")
        return False

    def get_profile(self):
        """Devuelve el perfil asociado o None si no existe."""
        if self.is_tourist():
            return getattr(self, "touristprofile", None)
        elif self.is_guide():
            return getattr(self, "guideprofile", None)
        return None

    def __str__(self):
        return self.username


class TouristProfile(models.Model):
    """Perfil adicional para usuarios turistas."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Tourist {self.user.username} ({self.country and self.country.name or 'No country'})"
    # favorite_birds = models.TextField(blank=True) # Todavía no se ha definido modelo para aves


class GuideProfile(models.Model):
    """Perfil adicional para usuarios guías."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, blank=True)
    experience_years = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Guide {self.user.username}"

# TODO: Aun no agrego perfil de operador porque no está en el MVP
# class OperatorProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    organization = models.CharField(max_length=200)
