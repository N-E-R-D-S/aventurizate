from django.apps import AppConfig
from django.db.models.signals import post_migrate
import pycountry


class AccountsConfig(AppConfig):
    """
    Configuración de la aplicación 'accounts'.

    - Define configuraciones específicas para la app de cuentas/usuarios.
    - Se encarga de conectar señales al iniciar la aplicación.
    - Usa la señal `post_migrate` para asegurarse de que ciertos datos
        iniciales (grupos, países, idiomas) estén creados en la base de datos.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """Método llamado automáticamente cuando la aplicación está lista.
        - Importa las señales de la aplicación.
        - Conecta funciones a la señal `post_migrate` para que se ejecuten
            después de aplicar migraciones en la base de datos."""
        import accounts.signals
        post_migrate.connect(create_user_groups, sender=self)
        post_migrate.connect(create_countries, sender=self)
        post_migrate.connect(create_languages, sender=self)


def create_user_groups(sender, **kwargs):
    """Crea los grupos de usuarios predeterminados en el sistema."""
    from django.contrib.auth.models import Group
    groups = ["Tourist", "Guide", "Operator"]
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)


def create_countries(sender, **kwargs):
    """Crea registros de países en la base de datos usando `pycountry`.
    Si un país ya existe en la base de datos, no se duplica."""
    from .models import Country
    for country in pycountry.countries:
        Country.objects.get_or_create(
            name=country.name,
            alpha_2=country.alpha_2,
            alpha_3=country.alpha_3,
            official_name=getattr(country, "official_name", country.name)
        )


def create_languages(sender, **kwargs):
    """Crea registros de idiomas en la base de datos usando `pycountry`.
    Si un idioma ya existe en la base de datos, no se duplica."""
    from .models import Language
    for lang in pycountry.languages:
        name = getattr(lang, "name", None)
        alpha_2 = getattr(lang, "alpha_2", None)
        alpha_3 = getattr(lang, "alpha_3", None)

        if name:
            # Solo crear si no existe un idioma con este alpha_2 o alpha_3
            if alpha_2:
                Language.objects.get_or_create(alpha_2=alpha_2, defaults={
                    "name": name,
                    "alpha_3": alpha_3
                })
            elif alpha_3:
                Language.objects.get_or_create(alpha_3=alpha_3, defaults={
                    "name": name,
                    "alpha_2": alpha_2
                })
            else:
                # Si no tiene alpha_2 ni alpha_3, solo se usa el nombre
                Language.objects.get_or_create(name=name)
