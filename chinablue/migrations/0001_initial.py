# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-18 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttenceInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attenceArr', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='TraineeInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('openid', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='attenceinfor',
            name='trainee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinablue.TraineeInfor'),
        ),
    ]
