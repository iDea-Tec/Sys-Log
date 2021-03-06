# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170531_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=60, verbose_name='Razão social')),
                ('nome_fantasia', models.CharField(max_length=60, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('inscricao_estadual', models.CharField(max_length=20, verbose_name='Incrição Estadual')),
                ('uf', models.CharField(max_length=25, verbose_name='UF')),
                ('cep', models.CharField(max_length=11, verbose_name='Cep')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('logradouro', models.CharField(max_length=40, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=60, verbose_name='E-mail')),
                ('latitude', models.CharField(max_length=25, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=25, verbose_name='Longitude')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
