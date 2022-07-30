from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from blog.forms import Buscar, Formulario
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

def crear(request):

    if request.method == 'POST':
        form = Formulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            fecha=data.get('fecha_creacion')

            publicacion = Publicacion(
                titulo=data.get('titulo'),
                subtitulo=data.get('subtitulo'),
                contenido=data.get('contenido'),
                autor=data.get('autor'),
                fecha_creacion=fecha if fecha else datetime.now() 
            )
            publicacion.save()

            publicaciones = Publicacion.objects.all()

            return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

        else:
            return render(request, 'crear.html', {'form': form} )


    formulario = Formulario()

    return render(request, 'crear.html', {'form': formulario} )



def publicaciones(request):

    buscar_titulo = request.GET.get('titulo')
    if buscar_titulo:
        publicaciones = Publicacion.objects.filter(titulo__icontains=buscar_titulo)
    else:
        publicaciones = Publicacion.objects.all()
    form = Buscar()

    return render(request, 'publicaciones.html', {'publicaciones': publicaciones, 'form': form})

