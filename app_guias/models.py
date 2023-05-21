from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=64) 
    apellido = models.CharField(max_length=64)# Equivalente de str
    area = models.CharField(max_length=64)  # Equivalent de int
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido} - {self.area}"

class Agentes(models.Model):
    nombre_fwr = models.CharField(max_length=64,db_column='Nombre de Agente:')  
    abrev_fwr = models.CharField(max_length=6,db_column='Abreviatura:')
    cotizador_fwr = models.CharField(max_length=64,blank=True,db_column='Cotizaciones:') 
    manager_fwr = models.CharField(max_length=64,blank=True,db_column='Agentes de Cuenta:')
    operativo_fwe =models.CharField(max_length=64,blank=True,db_column='Operativo Aereos:')
    ctc_fwr = models.TextField(db_column='Informacion extra:')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre_fwr}  {self.abrev_fwr}"
    
class Cargas(models.Model):
    ot=models.CharField(max_length=10,blank=True)
    mawb=models.CharField(max_length=12,blank=True)
    hawb=models.CharField(max_length=12,blank=True)
    incoterm = models.CharField(max_length=20,blank=True)
    area = models.CharField(max_length=64)
    abrev_fwr = models.CharField(max_length=6,blank=True,null=True)
    cotizacion = models.FloatField(blank=True,null=True)
    bultos = models.IntegerField(blank=True,null=True)
    peso = models.FloatField(blank=True,null=True)
    volumen = models.FloatField(blank=True,null=True)
    atd = models.DateField(blank=True,null=True)
    ata = models.DateField(blank=True,null=True)
    estado = models.CharField(max_length=12,blank=True,null=True)
    retiro = models.DateField(blank=True,null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.mawb}  {self.hawb}  {self.abrev_fwr} -- {self.estado}"
