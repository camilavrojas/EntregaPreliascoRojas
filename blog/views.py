from string import punctuation
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Publicacion

def inicio(request):
    return render(request, 'index.html')

def template(request):

    #template = loader.get_template('index.html')
    titulo1 = Publicacion(titulo="hola")
    titulo2 = Publicacion(titulo="como")
    titulo3 = Publicacion(titulo="estas")

    #render = template.render({'lista_objetos': [titulo1,titulo2, titulo3]})
    #return HttpResponse(render)
    return render(request,'mi_template.html', {'lista_objetos': [titulo1,titulo2, titulo3]})

def acerca(request):
    return render(request, 'acerca.html')

def publicaciones(request):
    return render(request, 'publicaciones.html')

def crear(request):
    return render(request, 'crear.html')
