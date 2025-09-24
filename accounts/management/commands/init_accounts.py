from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.models import Country, Language
import pycountry


class Command(BaseCommand):
    help = "Inicializa datos básicos de la app accounts (grupos, países, idiomas)."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Iniciando carga de datos..."))

        # Crear grupos
        groups = ["Tourist", "Guide", "Operator"]
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)
        self.stdout.write(self.style.SUCCESS("✅ Grupos creados."))

        # Crear países
        for country in pycountry.countries:
            Country.objects.get_or_create(
                name=country.name,
                alpha_2=country.alpha_2,
                alpha_3=country.alpha_3,
                official_name=getattr(country, "official_name", country.name)
            )
        self.stdout.write(self.style.SUCCESS("✅ Países cargados."))

        # Crear idiomas
        """for lang in pycountry.languages:
            name = getattr(lang, "name", None)
            alpha_2 = getattr(lang, "alpha_2", None)
            alpha_3 = getattr(lang, "alpha_3", None)

            if name:
                if alpha_2:
                    Language.objects.get_or_create(
                        alpha_2=alpha_2,
                        defaults={"name": name, "alpha_3": alpha_3}
                    )
                elif alpha_3:
                    Language.objects.get_or_create(
                        alpha_3=alpha_3,
                        defaults={"name": name, "alpha_2": alpha_2}
                    )
                else:
                    Language.objects.get_or_create(name=name)"""

        # self.stdout.write(self.style.SUCCESS("✅ Idiomas cargados."))
        self.stdout.write(self.style.SUCCESS("🚀 Inicialización completa."))
