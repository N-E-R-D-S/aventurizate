from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import TouristProfile, GuideProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal que se ejecuta automáticamente después de guardar un User.
    Lógica:
        - Cuando se crea un usuario (created=True), se verifica a qué grupo
            pertenece (ej. 'Tourist' o 'Guide').
        - Dependiendo del grupo, se crea el perfil correspondiente:
            - TouristProfile si es turista.
            - GuideProfile si es guía.
        - TODO: En el futuro, se puede extender para soportar otros perfiles
            como OperatorProfile.
    """
    if created:
        group = instance.get_group()

        if group == "Tourist":
            TouristProfile.objects.create(user=instance)

        elif group == "Guide":
            GuideProfile.objects.create(user=instance)

        # elif group == "Operator":
        #    OperatorProfile.objects.create(user=instance)
