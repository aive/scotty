# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0003_cottage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cottage',
            options={},
        ),
        migrations.RemoveField(
            model_name='cottage',
            name='addr1',
        ),
        migrations.RemoveField(
            model_name='cottage',
            name='cottageid',
        ),
        migrations.RemoveField(
            model_name='cottage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cottage',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='cottage',
            name='views',
        ),
        migrations.AddField(
            model_name='cottage',
            name='bio',
            field=models.TextField(blank=True, default='keine Angabe', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cottage',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cottage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]