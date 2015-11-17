#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
	nombre = models.CharField(max_length=45)

class Afp(models.Model):
	nombre = models.CharField(max_length=45)

class Salud(models.Model):
	nombre = models.CharField(max_length=45)

class Zonal(models.Model):
	nombre = models.CharField(max_length=20)

class CCosto(models.Model):
	nombre = models.CharField(max_length=50)

class Usuario(models.Model):
    User_id = models.IntegerField()
    rut = models.CharField(max_length=45)
    fecha_ingreso = models.DateField()
    zonal = models.ForeignKey(Zonal)
    afp =models.ForeignKey(Afp)
    salud = models.ForeignKey(Salud)
    ccosto = models.ForeignKey(CCosto)
    cargo = models.ForeignKey(Cargo)
    fecha_ingreso = models.DateField();
    vencimiento_licencia_conducir = models.DateField()
    direccion = models.CharField(max_length=100)

class Liquidacion(models.Model):
	Usuario_rut = models.CharField(max_length=15)
	mes = models.IntegerField()
	ano = models.IntegerField()

	zonal = models.CharField(max_length=20)
	c_costo = models.CharField(max_length=40)
	dias = models.IntegerField()
	sueldo = models.IntegerField()
	h_extras = models.IntegerField()
	bonos_impon = models.IntegerField()
	gratificacion = models.IntegerField()
	total_impon = models.IntegerField()
	movilizacion = models.IntegerField()
	colacion = models.IntegerField()
	otros_no_impon = models.IntegerField()
	asig_fam = models.IntegerField()
	total_no_impon = models.IntegerField()
	total_haberes = models.IntegerField()
	afp = models.IntegerField()
	seg_cesantia = models.IntegerField()
	cesantia_emp = models.IntegerField()
	sis = models.IntegerField()
	ahorro_afp = models.IntegerField()	
	salud = models.IntegerField()
	mutual = models.IntegerField()
	impto_unico = models.IntegerField()
	prestamo_ccaf = models.IntegerField()
	prestamos = models.IntegerField()
	anticipos = models.IntegerField()
	otros_dsctos = models.IntegerField()
	total_dsctos = models.IntegerField()
	liquido_pago = models.IntegerField()
	costo = models.IntegerField()
	bonos = models.IntegerField()
	costo_total = models.IntegerField()

	porcentaje_cotizacion = models.IntegerField()
	pactado = models.IntegerField()
	comision_produccion = models.IntegerField()
	semana_corrida = models.IntegerField()
	asignacion_viaticos = models.IntegerField()
	movilizacion_combustible = models.IntegerField()
	anticipo_combustible = models.IntegerField()
	anticipo_viatico = models.IntegerField()





