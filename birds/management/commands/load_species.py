from django.core.management.base import BaseCommand
from pygbif import occurrences
from django.db import transaction
from birds.models import Species, Family, Order, Genus, IUCNRedListCategory


class Command(BaseCommand):
    help = "Carga especies de aves observadas en Nicaragua desde GBIF a partir de 2024"

    def handle(self, *args, **kwargs):
        limit = 300  # GBIF máximo por request
        start = 0
        total_records = 1
        processed_species = 0
        total_species = 0

        CATEGORIES = [
            {"code": "NE", "name": "Not Evaluated",
                "description": "Species has not yet been evaluated against the criteria."},
            {"code": "DD", "name": "Data Deficient",
                "description": "Inadequate information to make a direct or indirect assessment."},
            {"code": "LC", "name": "Least Concern",
                "description": "Widespread and abundant taxa."},
            {"code": "NT", "name": "Near Threatened",
                "description": "Close to qualifying for or likely to qualify for a threatened category in the near future."},
            {"code": "VU", "name": "Vulnerable",
                "description": "High risk of endangerment in the wild."},
            {"code": "EN", "name": "Endangered",
                "description": "Very high risk of extinction in the wild."},
            {"code": "CR", "name": "Critically Endangered",
                "description": "Extremely high risk of extinction in the wild."},
            {"code": "EW", "name": "Extinct in the Wild",
                "description": "Known only to survive in cultivation, captivity or as a naturalized population outside its past range."},
            {"code": "EX", "name": "Extinct",
                "description": "No known individuals remaining."},
        ]

        for cat in CATEGORIES:
            obj, created = IUCNRedListCategory.objects.get_or_create(
                code=cat["code"],
                defaults={"name": cat["name"],
                          "description": cat["description"]}
            )

        self.stdout.write(self.style.NOTICE("Iniciando carga desde GBIF..."))

        while start < total_records:
            try:
                data = occurrences.search(
                    country="NI",      # Nicaragua
                    taxon_key=212,     # Aves
                    limit=limit,
                    start=start,
                    year="2024,2025",  # Solo descargar datos actuales
                )

                total_records = data["count"]
                results = data["results"]

                for occ in results:
                    sci_name = occ.get("species")
                    if not sci_name:
                        continue

                    common_name = occ.get("genericName") or sci_name
                    genus_name = occ.get("genus")
                    family_name = occ.get("family")
                    order_name = occ.get("order")
                    iucn_red_list_category_name = occ.get(
                        "iucnRedListCategory")

                    with transaction.atomic():
                        order, _ = Order.objects.get_or_create(
                            name=order_name)
                        family, _ = Family.objects.get_or_create(
                            name=family_name, order=order)
                        genus, _ = Genus.objects.get_or_create(
                            name=genus_name, family=family)
                        iucn_red_list_category = None
                        if iucn_red_list_category_name:
                            iucn_red_list_category = IUCNRedListCategory.objects.filter(
                                code__icontains=iucn_red_list_category_name)
                            if iucn_red_list_category.exists():
                                iucn_red_list_category = iucn_red_list_category.first()

                        species_obj, created = Species.objects.get_or_create(
                            scientific_name=sci_name,
                            defaults={
                                "common_name": common_name,
                                "genus": genus,
                                "iucn_red_list_category": iucn_red_list_category
                            }
                        )
                        if created:
                            total_species += 1

                        processed_species += 1

                start += limit
                self.stdout.write(self.style.SUCCESS(
                    f"Avance: {start}/{total_records} registros procesados "
                ))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error registrando especies/observaciones desde GBIF: {e}"))
                break

        self.stdout.write(self.style.SUCCESS(
            f"Carga finalizada 🚀 Total especies agregadas: {total_species}, "))
