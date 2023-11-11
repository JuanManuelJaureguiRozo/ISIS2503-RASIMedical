from ..models import Cita

def get_citas():
    queryset = Cita.objects.all()
    return (queryset)

def create_cita(form):
    info = form.save()
    info.save()
    return ()