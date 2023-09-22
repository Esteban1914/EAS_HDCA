from django import forms
from .models import ModBus,MODB_TYPE

class ModBusForm(forms.ModelForm):
    ip=forms.GenericIPAddressField(initial="0.0.0.0",widget=forms.TextInput(attrs={'class':'form-control'}))
    #type=forms.ChoiceField(choices=MODB_TYPE)
    class Meta:
        model=ModBus
        fields = "__all__"
        widgets = {
            'slug': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese un nombre'}),
            'type':forms.Select(attrs={'class':'form-control'}),
            'coil_conductor':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Coil de Conductividad'}),
            'coil_motor':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Coil del Motor'}),
            'coil_mode':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Coil del Tanque'}),
            'register_valve':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Registro de la Válvula'}),
            'register_tank':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Registro del Tanque'}),
            'register_cistern':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Registro de la Cisterna'}),
            'registers_output':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Registro de Salida de Control'}),
            'register_setpoint':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Registro de SetPoint'}),
        }
        
        
class ModBusIdent(forms.Form):
    interval=forms.IntegerField(label="Tiempo de Intervalo",min_value=0,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Intervalo de muestreo'}))
    samples =forms.IntegerField(label="Muestras por Intervalo",min_value=0,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Cantidad de Muestras'}))
    step=forms.IntegerField(label="Paso entre Muestras",min_value=0,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Paso de Muestreo'}))
    #interval=forms.IntegerField(min_value=0,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Intervalo de muestreo'}))
    #interval=forms.IntegerField(min_value=0,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Intervalo de muestreo'}))
    
    class Meta:
        fields = 'interval','samples','step'
        