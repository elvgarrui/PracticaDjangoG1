from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Banco(models.Model):
    entidadId = models.CharField(max_length=4)
    nombre = models.CharField(max_length=150)
    def __unicode__(self):
        return self.nombre
    
class Sucursales(models.Model):
    sucursalId = models.CharField(max_length=4)
    banco = models.ForeignKey(Banco)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    def __unicode__(self):
        return self.sucursalId

class Usuario(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

class Cuenta(models.Model):
    numero = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario)
    saldo = models.FloatField()
    def __unicode__(self):
        return self.numero
    