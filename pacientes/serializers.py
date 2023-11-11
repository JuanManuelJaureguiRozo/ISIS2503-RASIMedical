from rest_framework import serializers
from . import models


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'nombre', 'id', 'tipocita', 'time',)
        model = models.Paciente