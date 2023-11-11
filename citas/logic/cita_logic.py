from ..models import Cita

def get_citas():
    queryset = Cita.objects.all()
    return (queryset)

def get_cita_by_id(id):
    queryset = Cita.objects.get(id=id)
    return (queryset)

def create_cita(form):
    info = form.save()
    info.save()
    return ()