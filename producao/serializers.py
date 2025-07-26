from rest_framework import serializers
from .models import Maquina, Turno, ProducaoDiaria

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

class ProducaoDiariaSerializer(serializers.ModelSerializer):
    maquina = MaquinaSerializer(read_only=True)
    turno = TurnoSerializer(read_only=True)
    maquina_id = serializers.PrimaryKeyRelatedField(queryset=Maquina.objects.all(), source='maquina', write_only=True)
    turno_id = serializers.PrimaryKeyRelatedField(queryset=Turno.objects.all(), source='turno', write_only=True)

    class Meta:
        model = ProducaoDiaria
        fields = ['id', 'data', 'maquina', 'maquina_id', 'turno', 'turno_id', 'operador', 'total_produzido', 'codigo_agulha', 'ocorrencias']



from rest_framework import serializers
from .models import ProducaoDiaria, Maquina, Turno

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

class ProducaoDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducaoDiaria
        fields = '__all__'
