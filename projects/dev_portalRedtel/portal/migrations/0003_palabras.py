# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palabras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20)),
                ('palabra1', models.CharField(max_length=20)),
                ('palabra2', models.CharField(max_length=20)),
            ],
        ),
    ]
