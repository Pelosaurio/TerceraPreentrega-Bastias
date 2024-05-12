from django import forms
from . import models

class RegistrarUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario 
        fields = '__all__'
    nombre = forms.CharField
    fecha_nacimiento = forms.DateField
    telefono = forms.NumberInput
    correo = forms.EmailField
    usuario = forms.CharField
    contraseña = forms.PasswordInput