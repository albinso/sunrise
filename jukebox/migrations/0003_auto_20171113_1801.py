# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jukebox', '0002_playlist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]