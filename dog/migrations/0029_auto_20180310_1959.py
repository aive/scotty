# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0028_auto_20180310_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='region',
            name='slug',
            field=models.SlugField(),
        ),
    ]
