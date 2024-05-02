from django.db import models

CREADA = 'CREADA'
DESARROLLO = 'DESARROLLO'
COMPLETADA = 'COMPLETADA'

ESTADO_TAREA = {
    CREADA: 'Creada',
    DESARROLLO: 'Desarrollo',
    COMPLETADA: 'Completada'
}

class Tarea(models.Model):
    idTarea = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_TAREA, default=CREADA)
    # proyecto
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaLimite = models.DateTimeField()
    # categoria
    def __str__(self):
        return self.descripcion