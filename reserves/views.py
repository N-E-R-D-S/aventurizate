from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Reserve

reservePerPage = 12


def reserve_list(request):
    """
    Listado de reservas naturales con paginación
    """
    reserve_list = Reserve.objects.all().order_by('name')
    paginator = Paginator(reserve_list, reservePerPage)

    page_number = request.GET.get('page')
    reserves = paginator.get_page(page_number)

    context = {
        'reserves': reserves
    }
    return render(request, 'reserves/reserve_list.html', context)


def reserve_detail(request, pk):
    """
    Muestra la información de la reserva y las aves asociadas
    """
    reserve = get_object_or_404(Reserve, pk=pk)
    birds = reserve.birds.all()
    photos = reserve.reservephoto_set.all()
    context = {
        "reserve": reserve,
        "birds": birds,
        "photos": photos
    }
    return render(request, "reserves/reserve_detail.html", context)
