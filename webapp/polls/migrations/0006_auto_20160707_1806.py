# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160629_1909'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choices',
        ),
    ]
