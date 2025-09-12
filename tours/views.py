from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Tour, TourReservation


@login_required
def create_tour(request):
    if not request.user.is_guide():
        messages.error(request, "Solo los guías pueden crear tours.")
        return redirect("tour_list")

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        date = request.POST.get("date")
        max_participants = request.POST.get("max_participants")
        price = request.POST.get("price") or 0
        if not all([name, description, date, max_participants]):
            messages.error(request, "Todos los campos excepto el precio son obligatorios.")
            return render(request, "tours/create_tour.html")

        try:
            date = timezone.datetime.fromisoformat(date)
            max_participants = int(max_participants)
            price = float(price)
        except ValueError:
            messages.error(request, "Datos inválidos. Por favor verifica los campos.")
            return render(request, "tours/create_tour.html")

        new_tour = Tour.objects.create(
            name=name,
            description=description,
            date=date,
            max_participants=max_participants,
            price=price,
            guide=request.user.get_profile()
        )
        messages.success(request, "Tour creado con éxito.")
        return redirect("tour_detail", tour_id=new_tour.id)

    return render(request, "tours/create_tour.html")


def list_tours(request):
    tours = Tour.objects.filter(published=True)
    return render(request, "tours/tour_list.html", {"tours": tours})


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    context = {
        "tour": tour,
        "spots_taken": tour.spots_taken(),
        "spots_available": tour.spots_available(),
    }
    return render(request, "tours/tour_detail.html", context)

@login_required
def my_tours(request):
    if not request.user.is_guide():
        messages.error(request, "Solo los guías pueden ver sus tours.")
        return redirect("tour_list")

    tours = Tour.objects.filter(guide__user=request.user)
    context = {
        "tours": tours
    }
    return render(request, "tours/my_tours.html", context)

@login_required
def reserve_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id, published=True)

    if not request.user.is_tourist():
        messages.error(request, "Solo los turistas pueden reservar tours.")
        return redirect("tour_list")

    if tour.spots_available() <= 0:
        messages.error(request, "No hay cupos disponibles para este tour.")
        return redirect("tours_list")

    reservation, created = TourReservation.objects.get_or_create(
        tour=tour,
        tourist=request.user.touristprofile
    )

    if not created:
        messages.info(request, "Ya tienes una reserva para este tour.")
    else:
        messages.success(request, "Tu reserva fue registrada con éxito.")

    return redirect("my_reservations")


@login_required
def my_reservations(request):
    if not request.user.is_tourist():
        messages.error(request, "Solo los turistas pueden ver sus reservas.")
        return redirect("tours_list")

    reservations = TourReservation.objects.filter(
        tourist=request.user.touristprofile
    ).select_related("tour")
    context = {
        "reservations": reservations
    }
    return render(request, "tours/my_reservations.html", context)


@login_required
def tour_participants(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if not request.user.is_guide() or tour.guide.user != request.user:
        messages.error(
            request, "No tienes permiso para ver los participantes de este tour.")
        return redirect("tours_list")

    participants = tour.reservations.select_related("tourist__user")
    context = {
        "tour": tour,
        "participants": participants
    }
    return render(request, "tours/tour_participants.html", context)
