from django.db import models

# Create your models here.

class Resenna(models.Model):
    idResenna = models.IntegerField(primary_key=True, verbose_name="Id de Reseña")
    tipoResenna = models.CharField(max_length=15, verbose_name="Tipo de reseña")

    def __str__(self):
        return self.tipoResenna

class ComentarioC(models.Model):
    NombreC = models.CharField(max_length=40, primary_key=True, verbose_name="Nombre completo cliente")
    comentario = models.CharField(max_length=150, verbose_name="comentario")
    resenna = models.ForeignKey(Resenna, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreC