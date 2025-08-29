from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Reserve(models.Model):
    """
    Modelo que representa una Reserva Natural
    """
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    # Aves que se pueden encontrar en la reserva (Birds App)
    birds = models.ManyToManyField(
        "birds.Species", blank=True)

    # Relación con guías disponibles en la reserva
    guides = models.ManyToManyField(
        "accounts.GuideProfile",
        blank=True,
    )

    def __str__(self):
        return self.name
