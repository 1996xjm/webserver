# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-30 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinablue', '0005_auto_20180724_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunchInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lunchInforArr', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='LunchUserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]
