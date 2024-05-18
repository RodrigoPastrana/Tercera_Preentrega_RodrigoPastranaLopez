"""
URL configuration for DreamLeague project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Liga import views as liga_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", liga_views.inicio, name="inicio"),
    path("crear_division/", liga_views.crear_division, name="crear_division"),
    path("crear_equipo/", liga_views.crear_equipo, name="crear_equipo"),
    path("crear_jugador/", liga_views.crear_jugador, name="crear_jugador"),
    path("buscar_division/", liga_views.buscar_division, name="buscar_division"),
    ]
