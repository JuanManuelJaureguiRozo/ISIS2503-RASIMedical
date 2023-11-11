from django.db import models
from citas.models import Cita
from pacientes.models import Paciente

class Alarm(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, default=None)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(null=True, blank=True, default=None)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"cita": %s, "paciente": %s, "limitExceeded": %s, "dateTime": %s}' % (self.cita.name, self.paciente.nombre, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'cita': self.cita.name,
            'paciente': self.paciente.nombre,
            'nombre': self.nombre,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm