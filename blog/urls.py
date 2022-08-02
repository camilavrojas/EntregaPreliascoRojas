from django.urls import path
from .views import inicio, acerca, publicaciones, crear 
from . import views 

urlpatterns = [
    path('', inicio, name='index'), 
    path('acerca/', acerca, name='acerca'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('crear-publicacion/', crear, name='crear'),
    path('editar-publicacion/<int:pk>', views.Editar.as_view(), name='editar_publicacion'),
    path('eliminar-publicacion/<int:pk>', views.Eliminar.as_view(), name='eliminar_publicacion'),
    path('mostrar-publicacion/<int:pk>', views.Mostrar.as_view(), name='mostrar_publicacion')
]
