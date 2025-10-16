from django.db import models


class Tour(models.Model):
    """
    Representa un tour o visita guiada creado por un guía.
    """
    guide = models.ForeignKey(
        "accounts.GuideProfile",
        on_delete=models.CASCADE,
        related_name="tours"
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        unique_together = ("guide", "name", "date")

    def spots_taken(self):
        """Cantidad de participantes ya reservados."""
        return self.reservations.filter(is_confirmed=True).count()

    def spots_available(self):
        """Cupo restante disponible."""
        return self.max_participants - self.spots_taken()

    def __str__(self):
        return self.name


class TourReservation(models.Model):
    """
    Representa la reserva de un turista en un tour.
    """

    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name="reservations")
    tourist = models.ForeignKey(
        "accounts.TouristProfile", on_delete=models.CASCADE, related_name="tour_reservations")
    is_confirmed = models.BooleanField(default=False)
    reserved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("tour", "tourist")
        ordering = ["-reserved_at"]

    def __str__(self):
        return f"Reserva de {self.tourist.user.username} en {self.tour.name} ({self.is_confirmed})"
