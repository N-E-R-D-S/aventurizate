from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Species, Photo

birdPerPage = 12


def bird_list_view(request):
    """
    Vista para listar las aves con paginación
    """
    bird_list = Species.objects.all().select_related(
        "genus__family__order", "iucn_red_list_category"
    )
    paginator = Paginator(bird_list, birdPerPage)

    page_number = request.GET.get("page")
    birds = paginator.get_page(page_number)
    context = {"birds": birds}

    return render(request, "birds/bird_list.html", context)


def bird_detail_view(request, slug):
    """
    Vista para mostrar el detalle de un ave
    """
    bird = get_object_or_404(Species, slug=slug)
    photos = Photo.objects.filter(bird=bird)
    context = {"bird": bird, "photos": photos}

    return render(request, "birds/bird_detail.html", context)
