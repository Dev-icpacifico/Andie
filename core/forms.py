"""# andon/forms.py
from django import forms
from django.forms import TextInput, Textarea, Select
from .models import Alerta

class AlertaForm(forms.ModelForm):
    class Meta:
        model = Alerta
        fields = '__all__'
        widgets = {
            # Campos de texto cortos
            #'fecha_apertura': TextInput(attrs={'style': 'width: 150px;'}),
            # 'fecha_asignacion': TextInput(attrs={'style': 'width: 150px;'}),

            # Campos de texto largos
            # 'mensaje_alerta': Textarea(attrs={'rows': 2, 'cols': 60}),
            'partida_faena': Textarea(attrs={'rows': 2, 'cols': 60}),
            'observaciones_revision': Textarea(attrs={'rows': 2, 'cols': 60}),

            # Campos tipo select o foreign key
            'proyecto': Select(attrs={'style': 'width: 220px;'}),
            'edificio': Select(attrs={'style': 'width: 140px;'}),
            'piso': Select(attrs={'style': 'width: 30px;'}),
            'departamento': Select(attrs={'style': 'width: 30px;'}),
            'clasificacion_ia': Select(attrs={'style': 'width: 200px;'}),
            'urgencia_ia': Select(attrs={'style': 'width: 150px;'}),
            'estado_alerta': Select(attrs={'style': 'width: 50px;'}),
            'colaborador_reporta': Select(attrs={'style': 'width: 50px;'}),
            'unidad_operativa': Select(attrs={'style': 'width: 50px;'}),
        }
"""