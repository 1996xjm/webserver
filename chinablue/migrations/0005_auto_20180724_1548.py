# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-24 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinablue', '0004_chinablueuserinfor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinablueuserinfor',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chinablueuserinfor',
            name='userid',
            field=models.CharField(max_length=200, null=True),
        ),
    ]