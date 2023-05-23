from django import forms

class AgentesFormulario(forms.Form):
    nombre_fwr = forms.CharField(max_length=64,label= "Nombre:",required=True)  
    abrev_fwr = forms.CharField(max_length=6,label= "Identificador:",required=True)
    cotizador_fwr = forms.CharField(max_length=64,label= "Encargado Cotizaciones:",required=False)
    operativo_fwe = forms.CharField(max_length=64,label= "Encargado Operativo:",required=False)
    ctc_fwr  = forms.CharField(max_length=500,label= "Informacion extra:",required=False)
    
class UsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=64,label= "Nombre:",required=True) 
    apellido = forms.CharField(max_length=64,label= "Apellido:",required=True)
    area = forms.CharField(max_length=64,label= "Area de trabajo:",required=True) 
    email = forms.EmailField(label= "E-mail:",required=False)
    telefono = forms.CharField(max_length=20,label= "Telefono:",required=False) 
    
class CargasFormulario (forms.Form):
    ot=forms.CharField(max_length=10,label= "Numero de OT:",required=True)
    mawb=forms.CharField(max_length=12,label= "Guia Madre:",required=False)
    hawb=forms.CharField(max_length=12,label= "Guia Hija:",required=False)
    incoterm = forms.CharField(max_length=20,label= "Incoterm:",required=False)
    area = forms.CharField(max_length=64,label= "Area del usuario:",required=False)
    abrev_fwr = forms.CharField(max_length=6,label= "Identificador de Frw:",required=False)
    cotizacion = forms.FloatField(label= "Valor Cotizado:",required=False)
    bultos = forms.IntegerField(label= "Cantidad de bultos:",required=False)
    peso = forms.FloatField(label= "Peso total:",required=False)
    volumen = forms.FloatField(label= "Volumen:",required=False)
    atd = forms.DateField(label= "Fecha de ATD (MM/DD/AAA):",required=False)
    ata = forms.DateField(label= "Fecha de AAD (MM/DD/AAA):",required=False)
    estado = forms.CharField(max_length=12, label= "Estado:",required=False)
    retiro = forms.DateField(label= "Fecha de retiro de EZE (MM/DD/AAA):",required=False)
    
