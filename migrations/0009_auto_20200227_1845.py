# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-27 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabe_app', '0008_auto_20200227_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='knet',
            field=models.CharField(choices=[(True, 'Enable'), (False, 'Disable')], default='Enabaled', max_length=50, verbose_name='Knet Staus'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='mpgs',
            field=models.CharField(choices=[(True, 'Enable'), (False, 'Disable')], default='Disabled', max_length=50, verbose_name='Mpgs Staus'),
        ),
    ]