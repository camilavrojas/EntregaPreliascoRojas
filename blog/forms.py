from django import forms 

class Formulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=300)
    autor = forms.CharField(max_length=50)
    fecha_creacion = forms.DateField(required=False)

class Buscar(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
