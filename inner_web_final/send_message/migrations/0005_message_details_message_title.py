# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_message', '0004_auto_20161030_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_details',
            name='message_title',
            field=models.CharField(default=124, max_length=256, verbose_name='UUID'),
            preserve_default=False,
        ),
    ]
