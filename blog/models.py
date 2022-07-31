from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    fecha_creacion = models.DateField(null=True)

    def __str__(self):
        return f'Titulo: {self.titulo}'
