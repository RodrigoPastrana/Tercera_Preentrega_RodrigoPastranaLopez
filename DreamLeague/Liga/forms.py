from django import forms
from .models import División, Equipo, Jugador


class DivisiónForm(forms.ModelForm):
    class Meta:
        model = División
        fields = ["nombre"]


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "division"]


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "equipo"]

class DivisionSearchForm(forms.Form):
    query = forms.CharField(label='Buscar División', max_length=255)