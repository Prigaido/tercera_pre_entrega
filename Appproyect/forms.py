from django import forms

class ProfeForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class AlumForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class CursoForm(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()


class EntregaForm(forms.Form):
    nombre = forms.CharField()
    fechadeEntrega = forms.DateField()
    entregado = forms.BooleanField()
