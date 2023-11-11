from django.db import models
from citas.models import Cita

class Paciente(models.Model):
    nombre = models.ForeignKey(Cita, on_delete=models.CASCADE, default=None)
    id = models.FloatField(null=True, blank=True, default=None)
    tipocita = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.tipocita)