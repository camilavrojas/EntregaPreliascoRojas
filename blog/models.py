from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
  

#subtitulo = models.CharField(max_length=100)
#autor = models.CharField(max_length=50)
#fecha_creacion = models.DateField(null=True)
