from django.db import models

class Registro(models.Model):
    idRegistro=models.Autofield(primary_key=true)
    fechaInicio=models.DateTimeField(auto_now_add=true)
    fechaFin=models.DateTimeField()
    minutos=models.IntegerField()

    