from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .models import User, TouristProfile, GuideProfile
from birds.models import Species
from tours.models import Tour
from reserves.models import Reserve
import random

def index(request):
    # Obtener un ave aleatoria
    bird_count = Species.objects.count()
    random_bird = Species.objects.all()[random.randint(0, bird_count - 1)] if bird_count else None

    # Obtener un tour aleatorio publicado
    tours_qs = Tour.objects.filter(published=True)
    tour_count = tours_qs.count()
    random_tour = tours_qs[random.randint(0, tour_count - 1)] if tour_count else None

    # Obtener una reserva natural aleatoria
    reserve_count = Reserve.objects.count()
    random_reserve = Reserve.objects.all()[random.randint(0, reserve_count - 1)] if reserve_count else None

    context = {
        "random_bird": random_bird,
        "random_tour": random_tour,
        "random_reserve": random_reserve,
    }

    return render(request, "accounts/index.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("bird_list")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        password = request.POST.get("password", "")
        confirmation = request.POST.get("confirmation", "")
        if password != confirmation:
            context = {
                "message": "Passwords must match."
            }
            return render(request, "accounts/register.html", context)
        user_type = request.POST.get("user_type", "tourist")
        if user_type not in ["tourist", "guide"]:
            context = {
                "message": "Invalid user type."
            }
            return render(request, "accounts/register.html", context)
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            if user_type == "tourist":
                tourist = TouristProfile.objects.create(user=user)
                tourist.save()
                Group.objects.get(name='Tourist').user_set.add(user)
            if user_type == "guide":
                guide = GuideProfile.objects.create(user=user)
                guide.save()
                Group.objects.get(name='Guide').user_set.add(user)
        except Exception as e:
            context = {
                "message": "Username already taken."
            }
            return render(request, "accounts/register.html", context)
    return render(request, "accounts/register.html")
