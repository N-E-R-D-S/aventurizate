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

    birds = models.ManyToManyField(
        "birds.Species", blank=True)

    def __str__(self):
        return self.name


class ReservePhoto(models.Model):
    """
    Modelo para fotos de reservas
    """
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reserve_photos/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.reserve.name} - {self.description[:30]}"
