# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-29 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20180429_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
    ]