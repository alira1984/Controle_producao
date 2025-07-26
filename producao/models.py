from django.db import models

class Maquina(models.Model):
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.codigo


class Turno(models.Model):
    numero = models.PositiveSmallIntegerField(unique=True,
                                              choices=[(1, '1º Turno'), (2, '2º Turno'), (3, '3º Turno')])

    def __str__(self):
        return f"{self.numero}º Turno"


class ProducaoDiaria(models.Model):
    data = models.DateField()
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    operador = models.CharField(max_length=100)
    total_produzido = models.PositiveIntegerField()
    codigo_agulha = models.CharField(max_length=50)
    ocorrencias = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('data', 'turno', 'maquina')

    def __str__(self):
        return f"{self.data} - {self.maquina} - Turno {self.turno.numero}"
