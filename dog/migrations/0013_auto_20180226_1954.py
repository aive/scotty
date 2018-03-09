# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0012_auto_20180226_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='cottage',
            name='addr1',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='cottage',
            name='addr2',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='cottage',
            name='addr3',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='cottage',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='cottage',
            name='postcode',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='cottage',
            name='region',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='cottage',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
