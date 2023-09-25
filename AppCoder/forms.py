from django import forms

class MaquillajeFormulario(forms.Form):
    nombre = forms.CharField()
    color = forms.CharField()
    precio = forms.IntegerField()

class AccesorioFormulario(forms.Form):
    nombre = forms.CharField()
    color = forms.CharField()
    precio = forms.IntegerField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    contrasenia = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()  

