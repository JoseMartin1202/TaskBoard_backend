from django.db import models

# Create your models here.
class Proyecto(models.Model):
    idProyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    # creado_por = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre