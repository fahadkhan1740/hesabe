# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-01 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabe_app', '0010_auto_20200227_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='accesscode',
            field=models.CharField(default='SDfzsdf', max_length=455),
            preserve_default=False,
        ),
    ]
