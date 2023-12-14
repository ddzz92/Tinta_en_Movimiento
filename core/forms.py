from django import forms
from .models import Contacto, Turnos

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        
class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'