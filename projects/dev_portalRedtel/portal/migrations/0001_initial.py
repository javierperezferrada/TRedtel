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
                ('Usuario_rut', models.CharField(max_length=45)),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('porcentaje_cotizacion', models.IntegerField()),
                ('pactado', models.IntegerField()),
                ('dias_trabajados', models.IntegerField()),
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
                ('anticipo_combustible', models.IntegerField()),
                ('anticipo_viatico', models.IntegerField()),
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
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_id', models.IntegerField()),
                ('rut', models.CharField(max_length=45)),
                ('fecha_ingreso', models.DateField()),
                ('vencimiento_licencia_conducir', models.DateField()),
                ('Afp_id', models.ForeignKey(to='portal.Afp')),
                ('Area_id', models.ForeignKey(to='portal.Area')),
                ('Cargo_id', models.ForeignKey(to='portal.Cargo')),
                ('CentroCosto_id', models.ForeignKey(to='portal.CentroCosto')),
                ('Salud_id', models.ForeignKey(to='portal.Salud')),
            ],
        ),
    ]
