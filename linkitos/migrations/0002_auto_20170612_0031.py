# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkitos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
