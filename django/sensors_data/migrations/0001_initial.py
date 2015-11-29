# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('unixtime', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('sensortype', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='sensors_data.SensorType', blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='measure',
            name='unit',
            field=models.ForeignKey(to='sensors_data.Unit'),
        ),
        migrations.AddField(
            model_name='data',
            name='datatype',
            field=models.ForeignKey(to='sensors_data.DataType'),
        ),
        migrations.AddField(
            model_name='data',
            name='measure',
            field=models.ForeignKey(to='sensors_data.Measure'),
        ),
    ]
