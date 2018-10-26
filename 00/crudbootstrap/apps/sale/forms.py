from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'rut',
            'razon_social',
            'direccion',
            'comuna',
            'giro',
        ]