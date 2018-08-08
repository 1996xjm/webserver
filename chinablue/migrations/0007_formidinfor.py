# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-01 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chinablue', '0006_lunchinfor_lunchuserinfor'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormIdInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('formid', models.CharField(max_length=100)),
                ('chinablueuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinablue.ChinablueUserInfor')),
            ],
        ),
    ]