# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_testtask_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtask',
            name='result_time',
        ),
        migrations.AddField(
            model_name='testtask',
            name='result_ms',
            field=models.IntegerField(null=True),
        ),
    ]
