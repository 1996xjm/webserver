# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinablue', '0002_auto_20180718_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='traineeinfor',
            name='wxInfor',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
