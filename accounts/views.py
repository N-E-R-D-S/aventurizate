from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import User, TouristProfile, GuideProfile

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        password = request.POST.get("password", "")
        confirmation = request.POST.get("confirmation", "")
        if password != confirmation:
            context = {
                "message": "Passwords must match."
            }
            return render(request, "register.html", context)
        user_type = request.POST.get("user_type", "tourist")
        if user_type not in ["tourist", "guide"]:
            context = {
                "message": "Invalid user type."
            }
            return render(request, "register.html", context)
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
            return render(request, "register.html", context)
    return render(request, "register.html")