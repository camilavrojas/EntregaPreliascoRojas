from datetime import datetime
from django.shortcuts import redirect, render
from blog.forms import Formulario, Buscar
from .models import Publicacion
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import DetailView

def inicio(request):
    return render(request, 'index.html')

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

            return redirect('publicaciones')

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

# def editar(request, id):
#     publicacion = Publicacion.objects.get(id=id)

#     if request.method == 'POST':
#         form = Formulario(request.POST)
#         if form.is_valid():    
#             publicacion.titulo = form.cleaned_data.get('titulo')
#             publicacion.subtitulo = form.cleaned_data.get('subtitulo')
#             publicacion.contenido = form.cleaned_data.get('contenido')
#             publicacion.autor = form.cleaned_data.get('autor')
#             publicacion.fecha_creacion = form.cleaned_data.get('fecha_creacion')
#             publicacion.save()

#             return redirect('publicaciones')

#         else:
#             return render(request, 'editar.html', {'form': form, 'publicacion': publicacion })

#     formulario = Formulario(initial={'titulo': publicacion.titulo, 'subtitulo': publicacion.subtitulo, 'contenido': publicacion.contenido , 'autor': publicacion.autor, 'fecha_creacion':publicacion.fecha_creacion} )

#     return render(request, 'editar.html', {'form': formulario,'publicacion': publicacion } )
 

class Editar(UpdateView):
    model=Publicacion
    template_name= 'editar.html'
    success_url='/publicaciones'
    fields= ['titulo', 'subtitulo', 'contenido', 'autor']


class Eliminar(DeleteView):
    model=Publicacion
    template_name= 'eliminar.html'
    success_url='/publicaciones'


class Mostrar(DetailView):
    model=Publicacion
    template_name= 'mostrar.html'