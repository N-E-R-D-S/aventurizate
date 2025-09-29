from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.files.base import ContentFile
from .models import Species, Photo
from django.db.models import Q
from .pygbif_helper import get_gbif_taxon_key, get_species_distribution, get_gbif_photos, optimize_image, get_species_occurrences
import requests


birdPerPage = 12


def bird_list_view(request):
    """
    Vista para listar las aves con paginación
    """
    query = request.GET.get("q", "")
    bird_list = Species.objects.all().select_related(
        "genus__family__order", "iucn_red_list_category"
    ).order_by("scientific_name")
    if query:
        bird_list = bird_list.filter(
            Q(common_name__icontains=query) |
            Q(scientific_name__icontains=query) |
            Q(description__icontains=query)
        )
    paginator = Paginator(bird_list, birdPerPage)

    page_number = request.GET.get("page")
    birds = paginator.get_page(page_number)
    context = {"birds": birds, "query": query}

    return render(request, "birds/bird_list.html", context)


def bird_detail_view(request, slug):
    """
    Vista para mostrar el detalle de un ave
    """
    bird = get_object_or_404(Species, slug=slug)
    photos = Photo.objects.filter(bird=bird)

    gbif_key = get_gbif_taxon_key(bird.scientific_name)
    distribution_points = []
    if gbif_key:
        distribution_points = get_species_occurrences(gbif_key, limit=300)

    # Buscar hasta 3 fotos si no existen en la BD
    if not photos.exists() and gbif_key:
        gbif_photos = get_gbif_photos(gbif_key, max_photos=3)
        for idx, p in enumerate(gbif_photos, start=1):
            try:
                resp = requests.get(p["url"], timeout=10)
                if resp.status_code == 200:
                    optimized = optimize_image(resp.content)
                    file_name = f"{bird.slug}_{idx}.jpg"
                    photo = Photo(
                        bird=bird,
                        description=f"Foto de {bird.common_name} - "
                                    f"Autor: {p['creator']}, Fuente: {p['publisher']}"
                    )
                    photo.image.save(
                        file_name, ContentFile(optimized), save=True)
            except Exception as e:
                print("Error al guardar foto de GBIF:", e)
    context = {
        "bird": bird,
        "photos": Photo.objects.filter(bird=bird),
        "distribution_points": distribution_points,
    }

    return render(request, "birds/bird_detail.html", context)
