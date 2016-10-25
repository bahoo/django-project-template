# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 22:31
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CongressionalDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ('title', 'state__title'),
                'verbose_name': 'Congressional District',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('fips', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('title', 'state__title'),
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='LegislativeDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Legislative District',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('fips', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='legislativedistrict',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.State'),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.State'),
        ),
        migrations.AddField(
            model_name='congressionaldistrict',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.State'),
        ),
    ]
