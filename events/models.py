from django.db import models
from reserves.models import Reserve
from django.conf import settings


class Event(models.Model):
    """
    Evento de aviturismo.
    Ejemplo: Festival en la reserva, sendero privado, viaje personalizado, etc.
    """
    reserve = models.ForeignKey(
        Reserve,
        on_delete=models.CASCADE,
        related_name="events",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        "accounts.GuideProfile",
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        if self.reserve:
            return f"{self.title} - {self.reserve.name}"
        return f"{self.title} - Evento independiente"
