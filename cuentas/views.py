from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from cuentas.models import MasDatos 
from .forms import MyUserCreationForm, MyUserEditForm

def iniciar_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            usuario = authenticate(username=nombre_usuario, password=clave)

            if usuario is not None: 
                login(request,usuario)
                return render(request, 'index.html', {})
            else:
                return render(request, 'cuentas/iniciar_sesion.html', {'form': form})
      
        else:
            return render(request, 'cuentas/iniciar_sesion.html', {'form': form})


    form = AuthenticationForm()
    return render(request, 'cuentas/iniciar_sesion.html', {'form': form} )


def registrarse(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'cuentas/registrarse.html', {'form': form})

    form = MyUserCreationForm()
    return render(request, 'cuentas/registrarse.html', {'form': form} )


def perfil(request):
    return render(request, 'cuentas/perfil.html')

def editar_perfil(request):

    user = request.user
    mas_datos, _ = MasDatos.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid(): 
            data = form.cleaned_data 

            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos.avatar = data.get('avatar') if data.get('avatar') else mas_datos.avatar
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            mas_datos.save()
            user.save()

            return redirect('perfil')

        else:
            return render(request, 'cuentas/editar_perfil.html', {'form': form})

    # formulario = Formulario(initial={'titulo': publicacion.titulo, 'subtitulo': publicacion.subtitulo, 'contenido': publicacion.contenido , 'autor': publicacion.autor, 'fecha_creacion':publicacion.fecha_creacion} )
    form = MyUserEditForm(
        initial={
            'email': user.email, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'avatar': mas_datos.avatar
        } )
    return render(request, 'cuentas/editar_perfil.html', {'form': form})

