from django import forms
from .models import *
class ArtistaForm(forms.ModelForm):
    class Meta:
        
        model=Artista
        fields='__all__'
class CancionForm(forms.ModelForm):
    class Meta:
        model=Cancion
        fields='__all__'       