from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {"error": "Username already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

        return render(request, "accounts/login.html", {"error": "Invalid Username or Password"})

    return render(request, "accounts/login.html")


def logout_page(request):
    logout(request)
    return redirect("login")