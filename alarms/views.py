from django.http import JsonResponse
from django.shortcuts import render

from citas.logic.cita_logic import get_cita_by_id
from .logic.logic_alarm import get_alarms, get_pacientes_by_cita, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, cita_id):
    cita = get_cita_by_id(cita_id)
    pacientes = get_pacientes_by_cita(cita_id)
    createAlarm = False
    upperMeasurement = None
    for paciente in pacientes:
        if paciente.nombre == 'Carlos':
            createAlarm = True
            upperMeasurement = paciente
    if createAlarm:
        alarm = create_alarm(cita, upperMeasurement, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)