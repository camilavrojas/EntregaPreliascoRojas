from django.urls import path
from .views import inicio, acerca, publicaciones, crear, editar, eliminar, mostrar

urlpatterns = [
    path('', inicio, name='index'), 
    path('acerca/', acerca, name='acerca'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('crear-publicacion/', crear, name='crear'),
    path('editar-publicacion/<int:id>', editar, name='editar_publicacion'),
    path('eliminar-publicacion/<int:id>', eliminar, name='eliminar_publicacion'),
     path('mostrar-publicacion/<int:id>', mostrar, name='mostrar_publicacion')
]
