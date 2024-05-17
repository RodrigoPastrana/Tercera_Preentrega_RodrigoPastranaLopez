from django.shortcuts import render, redirect
from .forms import DivisiónForm, EquipoForm, JugadorForm
from .models import División, Equipo, Jugador
from .search_forms import DivisionSearchForm, EquipoSearchForm, JugadorSearchForm


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


def buscar_division(request):
    form = DivisionSearchForm()
    resultados = None
    if "query" in request.GET:
        form = DivisionSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = División.objects.filter(nombre__icontains=query)
    return render(request, "liga/buscar_division.html", {"form": form, "resultados": resultados})


def buscar_equipo(request):
    form = EquipoSearchForm()
    resultados = None
    if "query" in request.GET:
        form = EquipoSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Equipo.objects.filter(nombre__icontains=query)
    return render(request, "liga/buscar_equipo.html", {"form": form, "resultados": resultados})


def buscar_jugador(request):
    form = JugadorSearchForm()
    resultados = None
    if "query" in request.GET:
        form = JugadorSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Jugador.objects.filter(nombre__icontains=query)
    return render(request, "liga/buscar_jugador.html", {"form": form, "resultados": resultados})
