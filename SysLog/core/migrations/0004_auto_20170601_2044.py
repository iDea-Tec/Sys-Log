# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_relacionamento', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='clientes',
            field=models.ManyToManyField(through='core.ClienteEmpresa', to='core.Cliente'),
        ),
    ]
