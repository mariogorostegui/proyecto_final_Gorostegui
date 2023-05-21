from django import forms

class AgentesFormulario(forms.Form):
    nombre_fwr = forms.CharField(max_length=64)  
    abrev_fwr = forms.CharField(max_length=6) 
    ctc_fwr = forms.CharField()
    
class UsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=64) 
    apellido = forms.CharField(max_length=64)
    area = forms.CharField(max_length=64)  
    
class CargasFormulario (forms.Form):
    mawb=forms.CharField(max_length=12)
    hawb=forms.CharField(max_length=12)
    incoterm = forms.CharField(max_length=20)
    area = forms.CharField(max_length=64)
    abrev_fwr = forms.CharField(max_length=6)
    cotizacion = forms.FloatField()
    bultos = forms.IntegerField()
    peso = forms.FloatField()
    volumen = forms.FloatField()
    atd = forms.DateField()
    ata = forms.DateField()
    estado = forms.CharField(max_length=12)
    retiro = forms.DateField()