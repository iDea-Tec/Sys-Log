# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
    ]
