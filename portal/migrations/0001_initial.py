# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CentroCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut_trabajador', models.CharField(max_length=12)),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('sueldo', models.IntegerField()),
                ('gratificacion', models.IntegerField()),
                ('comision_produccion', models.IntegerField()),
                ('semana_corrida', models.IntegerField()),
                ('asignacion_viaticos', models.IntegerField()),
                ('movilizacion_combustible', models.IntegerField()),
                ('afp', models.IntegerField()),
                ('adiciona_afp', models.IntegerField()),
                ('salud', models.IntegerField()),
                ('seg_cesantia', models.IntegerField()),
                ('anticipo', models.IntegerField()),
                ('ant_combustible', models.IntegerField()),
                ('ant_viatico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('ingreso', models.DateField()),
                ('rut', models.CharField(max_length=12)),
                ('f_nacimiento', models.DateField()),
                ('vencimiento_lic_conducir', models.DateField()),
                ('id_afp', models.ForeignKey(to='portal.Afp')),
                ('id_area', models.ForeignKey(to='portal.Area')),
                ('id_cargo', models.ForeignKey(to='portal.Cargo')),
                ('id_ccosto', models.ForeignKey(to='portal.CentroCosto')),
                ('id_salud', models.ForeignKey(to='portal.Salud')),
            ],
        ),
    ]
