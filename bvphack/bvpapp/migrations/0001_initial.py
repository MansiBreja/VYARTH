# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-04 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('communityName', models.TextField(max_length=256)),
                ('address', models.TextField(max_length=1024)),
                ('contact', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]