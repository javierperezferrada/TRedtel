#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

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

class Usuario(models.Model):
    User_id = models.IntegerField()
    rut = models.CharField(max_length=45)
    fecha_ingreso = models.DateField()
    Area_id = models.IntegerField()
    Afp_id = models.IntegerField()
    Salud_id = models.IntegerField()
    CentroCosto_id = models.IntegerField()
    vencimiento_licencia_conducir = models.DateField()
    Cargo_id = models.IntegerField()

class Liquidacion(models.Model):
	Usuario_rut = models.CharField(max_length=45)
	mes = models.IntegerField()
	ano = models.IntegerField()
	porcentaje_cotizacion = models.IntegerField()
	pactado = models.IntegerField()
	dias_trabajados = models.IntegerField()
	sueldo = models.IntegerField()
	gratificacion = models.IntegerField()
	comision_produccion = models.IntegerField()
	semana_corrida = models.IntegerField()
	asignacion_viaticos = models.IntegerField()
	movilizacion_combustible = models.IntegerField()
	afp = models.IntegerField()
	adiciona_afp = models.IntegerField()
	salud = models.IntegerField()
	seguro_cesantia = models.IntegerField()
	anticipo = models.IntegerField()
	anticipo_combustible = models.IntegerField()
	anticipo_viatico = models.IntegerField()





