from django.core.management.base import BaseCommand
from pygbif import occurrences
from django.db import transaction
from birds.models import BirdSpecies, BirdFamily, BirdOrder, BirdGenus, BirdObservation


class Command(BaseCommand):
    help = "Carga especies y observaciones de aves para Nicaragua desde GBIF"

    def handle(self, *args, **kwargs):
        limit = 300  # GBIF máximo por request
        start = 0
        total_records = 1
        processed_species = 0
        processed_obs = 0

        self.stdout.write(self.style.NOTICE("Iniciando carga desde GBIF..."))

        while start < total_records:
            try:
                data = occurrences.search(
                    country="NI",      # Nicaragua
                    taxon_key=212,     # Aves
                    limit=limit,
                    start=start,
                    year=2025,  # Solo descargar datos actuales
                )

                total_records = data["count"]
                results = data["results"]

                for occ in results:
                    sci_name = occ.get("species")
                    if not sci_name:
                        continue

                    common_name = occ.get("vernacularName") or sci_name
                    genus_name = occ.get("genus")
                    family_name = occ.get("family")
                    order_name = occ.get("order")

                    with transaction.atomic():
                        order, _ = BirdOrder.objects.get_or_create(
                            name=order_name)
                        family, _ = BirdFamily.objects.get_or_create(
                            name=family_name, order=order)
                        genus, _ = BirdGenus.objects.get_or_create(
                            name=genus_name, family=family)

                        species_obj, created = BirdSpecies.objects.get_or_create(
                            scientific_name=sci_name,
                            defaults={
                                "common_name": common_name,
                                "genus": genus,
                            }
                        )

                        processed_species += 1
                        status = "creada" if created else "existente"
                        self.stdout.write(
                            f"[{processed_species}/{total_records}] Especie {sci_name} ({status})"
                        )

                        # Crear observación si hay coordenadas
                        lat = occ.get("decimalLatitude")
                        lon = occ.get("decimalLongitude")
                        date_observed = occ.get("eventDate")
                        gbif_id = occ.get("key") or occ.get("occurrenceID")

                        if lat and lon and gbif_id:
                            obs, created_obs = BirdObservation.objects.get_or_create(
                                gbif_id=str(gbif_id),
                                defaults={
                                    "bird": species_obj,
                                    "latitude": lat,
                                    "longitude": lon,
                                    "date_observed": date_observed[:10] if date_observed else None,
                                    "count": occ.get("individualCount") or 1,
                                    "note": occ.get("occurrenceRemarks") or "",
                                    "observer": None,  # No tenemos datos del usuario
                                }
                            )
                            if created_obs:
                                processed_obs += 1

                start += limit
                self.stdout.write(self.style.SUCCESS(
                    f"Avance: {start}/{total_records} registros procesados "
                    f"(Obs nuevas: {processed_obs})"
                ))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error registrando especies/observaciones desde GBIF: {e}"))
                break

        self.stdout.write(self.style.SUCCESS(
            f"Carga finalizada 🚀 Total especies procesadas: {processed_species}, "
            f"Observaciones nuevas: {processed_obs}"
        ))
