from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from .models import TourReservation

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == ST_PP_COMPLETED:
        try:
            reservation_id = int(ipn.custom)
            reservation = TourReservation.objects.get(id=reservation_id)
            reservation.is_paid = True
            reservation.save()
        except Exception as e:
            print("Error procesando IPN:", e)
