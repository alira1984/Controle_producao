from django import forms
from .models import ProducaoDiaria

class ProducaoDiariaForm(forms.ModelForm):
    class Meta:
        model = ProducaoDiaria
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'operador': forms.TextInput(attrs={'class': 'form-control'}),
            'total_produzido': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_agulha': forms.TextInput(attrs={'class': 'form-control'}),
            'ocorrencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'maquina': forms.Select(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
        }
