# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 04:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_end_date',
            new_name='journey_date',
        ),
    ]
