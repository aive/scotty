# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0021_cottage_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cottage',
            name='region',
            field=models.CharField(choices=[('', 'Aberdeenshire'), ('', 'Argyll'), ('', 'Ayrshire'), ('', 'Dumfries & Galloway'), ('', 'Angus'), ('', 'Edinburgh'), ('', 'Fife'), ('', 'Greater Glasgow'), ('', 'Highlands'), ('', 'Loch Lomond / Trossachs'), ('', 'Orkney'), ('', 'Outer Hebrides'), ('', 'Perthshire'), ('', 'Scottish Borders'), ('', 'Shetland')], max_length=128),
        ),
    ]