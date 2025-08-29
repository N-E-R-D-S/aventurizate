from django.db import models


class BookingStatus(models.Model):
    """Catálogo de estados posibles para una reserva"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """Reserva de un turista con guía o institución"""
    tourist = models.ForeignKey("Tourist", on_delete=models.CASCADE)
    guide = models.ForeignKey(
        "Guide", on_delete=models.SET_NULL, null=True, blank=True)
    reserve = models.ForeignKey("Reserve", on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(BookingStatus, on_delete=models.PROTECT)

    def __str__(self):
        return f"Reserva {self.id} - {self.tourist} ({self.status})"
