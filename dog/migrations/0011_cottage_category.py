# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dog', '0010_remove_cottage_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cottage',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
