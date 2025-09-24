from pygbif import species, occurrences
from io import BytesIO
from PIL import Image


def get_gbif_taxon_key(scientific_name):
    res = species.name_backbone(name=scientific_name)
    return res.get("usageKey")


def get_species_distribution(taxon_key, limit=100):
    occ = occurrences.search(
        taxonKey=taxon_key, limit=limit, hasCoordinate=True)
    points = [
        {"lat": r["decimalLatitude"], "lng": r["decimalLongitude"]}
        for r in occ["results"]
        if "decimalLatitude" in r and "decimalLongitude" in r
    ]
    return points


def get_gbif_photos(taxon_key, limit=10, max_photos=3):
    """
    Devuelve hasta `max_photos` fotos de GBIF para una especie.
    Incluye URL, autores y fuente en cada dict.
    """
    from pygbif import occurrences

    occ = occurrences.search(
        taxonKey=taxon_key, limit=limit, mediaType="StillImage")
    photos = []
    for r in occ.get("results", []):
        media = r.get("media", [])
        for m in media:
            if m.get("identifier"):  # URL de la foto
                photos.append({
                    "url": m["identifier"],
                    "creator": m.get("creator", "Desconocido"),
                    "publisher": m.get("publisher", "GBIF"),
                })
                if len(photos) >= max_photos:
                    return photos
    return photos


def optimize_image(image_bytes, max_size=(1024, 1024), quality=75):
    """
    Optimiza la imagen para reducir peso:
    - Redimensiona si es muy grande
    - Ajusta calidad JPEG
    """
    img = Image.open(BytesIO(image_bytes))
    img = img.convert("RGB")  # Asegurar formato consistente
    img.thumbnail(max_size, Image.Resampling.LANCZOS)

    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)
    return buffer.getvalue()


def get_species_occurrences(taxon_key, limit=300):
    """
    Obtiene ocurrencias recientes de una especie con coordenadas
    """
    occ = occurrences.search(
        taxonKey=taxon_key,
        hasCoordinate=True,
        limit=limit,
        mediaType=None,
        country="NI"
    )
    sightings = []
    for r in occ.get("results", []):
        if "decimalLatitude" in r and "decimalLongitude" in r:
            sightings.append({
                "lat": r["decimalLatitude"],
                "lng": r["decimalLongitude"],
            })
    return sightings
