# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_palabras'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Palabras',
            new_name='Palabra',
        ),
    ]
