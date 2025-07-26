from rest_framework import viewsets
from .models import ProducaoDiaria, Maquina, Turno
from .serializers import ProducaoDiariaSerializer, MaquinaSerializer, TurnoSerializer

class ProducaoDiariaViewSet(viewsets.ModelViewSet):
    queryset = ProducaoDiaria.objects.all()
    serializer_class = ProducaoDiariaSerializer

class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
