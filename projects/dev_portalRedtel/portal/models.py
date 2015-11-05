#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

#clase de prueba carga de csv
class Palabra(models.Model):
	tipo = models.CharField(max_length=20)
	palabra1 = models.CharField(max_length=20)
	palabra2 = models.CharField(max_length=20)
#fin clase de prueba

class Usuario(models.Model):
	nombre = models.CharField(max_length=20)
	rut = models.CharField(max_length=20)

#----------------------------------------------------
# Clases propuestas por el cliente.
#----------------------------------------------------
class Cargo(models.Model):
	nombre = models.CharField(max_length=30)

class Afp(models.Model):
	nombre = models.CharField(max_length=30)

class Salud(models.Model):
	nombre = models.CharField(max_length=30)

class Area(models.Model):
	nombre = models.CharField(max_length=30)

class CentroCosto(models.Model):
	nombre = models.CharField(max_length=30)

#----------------------------------------------------
# Fin Clases propuestas por el cliente.
#----------------------------------------------------

class Liquidacion(models.Model):
	rut_trabajador = models.CharField(max_length=12)
	mes = models.IntegerField()
	ano = models.IntegerField()
	sueldo = models.IntegerField()
	gratificacion = models.IntegerField()
	comision_produccion = models.IntegerField()
	semana_corrida = models.IntegerField()
	asignacion_viaticos = models.IntegerField()
	movilizacion_combustible = models.IntegerField()
	afp = models.IntegerField()
	adiciona_afp = models.IntegerField()
	salud = models.IntegerField()
	seg_cesantia = models.IntegerField()
	anticipo = models.IntegerField()
	ant_combustible = models.IntegerField()
	ant_viatico = models.IntegerField()

class Trabajador(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=150)
	id_cargo = models.ForeignKey(Cargo) 
	ingreso = models.DateField()
	id_afp = models.ForeignKey(Afp) 
	id_salud = models.ForeignKey(Salud) 
	rut = models.CharField(max_length=12)
	f_nacimiento = models.DateField()
	id_area = models.ForeignKey(Area) 
	id_ccosto = models.ForeignKey(CentroCosto) 
	vencimiento_lic_conducir = models.DateField()


