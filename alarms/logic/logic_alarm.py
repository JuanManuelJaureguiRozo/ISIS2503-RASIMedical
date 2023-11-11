from pacientes.models import Paciente
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_pacientes_by_cita(cita):
    queryset = Paciente.objects.filter(cita=cita).order_by('-dateTime')[:10]
    return (queryset)

def create_alarm(cita, paciente, limitExceeded):
    alarm = Alarm()
    alarm.cita = cita
    alarm.paciente = paciente
    alarm.nombre = paciente.nombre
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm