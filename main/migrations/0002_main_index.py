# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-02 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='index',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
