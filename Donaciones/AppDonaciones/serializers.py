from rest_framework import serializers
from .models import Donacion


class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = [
            "id",
            "fecha_creacion",
            "titulo",
            "descripcion",
            "imagen",
            "propietario",
            "telefono",
        ]
