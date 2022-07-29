from django.urls import path
from .views import inicio, template, acerca, publicaciones, crear

urlpatterns = [
    path('', inicio, name='index'), 
    path('template/', template),
    path('acerca/', acerca, name='acerca'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('crear/', crear, name='crear')
]
