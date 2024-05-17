from django.shortcuts import render, redirect
from .forms import DivisiónForm, EquipoForm, JugadorForm
from .models import División, Equipo, Jugador


def inicio(request):
    return render(request, "liga/inicio.html")


def crear_division(request):
    if request.method == "POST":
        form = DivisiónForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = DivisiónForm()
    return render(request, "liga/crear_division.html", {"form": form})


def crear_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = EquipoForm()
    return render(request, "liga/crear_equipo.html", {"form": form})


def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = JugadorForm()
    return render(request, "liga/crear_jugador.html", {"form": form})
