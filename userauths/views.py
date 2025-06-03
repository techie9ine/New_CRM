from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm


# Create your views here.


def home(request):

    context = {}
    return render(request, "core/home.html", context)


def signup(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"username {username} created successfully")
            return redirect("userauths:login")
    context = {"form": form}
    return render(request, "userauths/signu.html", context)


def login_view(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect("core:home")

    context = {"form": form}
    return render(request, "userauths/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect("userauths:login")








